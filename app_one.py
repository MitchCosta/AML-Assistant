



#from langchain.chat_models import ChatOpenAI
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.runnable.config import RunnableConfig

from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient, models
from langchain_openai.embeddings import OpenAIEmbeddings

from langchain.retrievers import MultiQueryRetriever

from operator import itemgetter

import chainlit as cl

import os
import getpass
from uuid import uuid4


#os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_PROJECT"] = f"AML-au - {uuid4().hex[0:8]}"
#os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("LangSmith_API_Key: ")
     


model = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)	#temperature=0.7

# Create Qdrant vectorstore as a retreiver
client = QdrantClient(path="Qdrant_db")
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

collection_name = "AML_act"
qdrant =  Qdrant(client, collection_name, embedding_model)

qdrant_retriever = qdrant.as_retriever()
advanced_retriever = MultiQueryRetriever.from_llm(retriever=qdrant_retriever, llm=model)

# FROM THE LOADER
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain.tools.retriever import create_retriever_tool

retreiver_tool = create_retriever_tool(
    advanced_retriever,
    "search_aml_act_retriever",
    "Searches and returns excerpts from the aml act in australia.",
)

tool_belt = [DuckDuckGoSearchRun(), retreiver_tool] 

from langgraph.prebuilt import ToolExecutor

tool_executor = ToolExecutor(tool_belt)

model_aml = ChatOpenAI(temperature=0)

from langchain_core.utils.function_calling import convert_to_openai_function

functions = [convert_to_openai_function(t) for t in tool_belt]
model_aml = model_aml.bind_functions(functions)

from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
  messages: Annotated[list, add_messages]
  
  
from langgraph.prebuilt import ToolInvocation
import json
from langchain_core.messages import FunctionMessage

def call_model(state):
  messages = state["messages"]
  response = model_aml.invoke(messages)
  return {"messages" : [response]}

def call_tool(state):
  last_message = state["messages"][-1]

  action = ToolInvocation(
      tool=last_message.additional_kwargs["function_call"]["name"],
      tool_input=json.loads(
          last_message.additional_kwargs["function_call"]["arguments"]
      )
  )

  response = tool_executor.invoke(action)

  function_message = FunctionMessage(content=str(response), name=action.tool)

  return {"messages" : [function_message]}

from langgraph.graph import StateGraph, END

workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)
workflow.add_node("action", call_tool)

workflow.set_entry_point("agent")

def should_continue(state):
  last_message = state["messages"][-1]

  if "function_call" not in last_message.additional_kwargs:
    return "end"

  return "continue"

workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue" : "action",
        "end" : END
    }
)

workflow.add_edge("action", "agent")

app = workflow.compile()

from langchain_core.messages import HumanMessage

inputs = {"messages" : [HumanMessage(content="where are  the aml ctf rules")]}

#messages = app.invoke(inputs)

def print_messages(messages):
  next_is_tool = False
  initial_query = True
  for message in messages["messages"]:
    if "function_call" in message.additional_kwargs:
      print()
      print(f'Tool Call - Name: {message.additional_kwargs["function_call"]["name"]} + Query: {message.additional_kwargs["function_call"]["arguments"]}')
      next_is_tool = True
      continue
    if next_is_tool:
      print(f"Tool Response: {message.content}")
      next_is_tool = False
      continue
    if initial_query:
      print(f"Initial Query: {message.content}")
      print()
      initial_query = False
      continue
    print()
    print(f"Agent Response: {message.content}")


@cl.on_chat_start
async def on_chat_start():

    RAG_PROMPT = """

    QUERY:
    {question}

    Answer the query above using the context provided. If you don't know the answer responde with: I don't know
    """

    rag_prompt = ChatPromptTemplate.from_template(RAG_PROMPT)
    """
    runnable = (
    {"context": itemgetter("question") | advanced_retriever, "question": itemgetter("question")}
    | RunnablePassthrough.assign(context=itemgetter("context"))
    | rag_prompt 
    | model | StrOutputParser()
    )
    """
    runnable =  app  # |  StrOutputParser()
    #runnable = {"messages" : "where are  the aml ctf rules"} | app |  StrOutputParser()

    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):

    
    
    print("Query content----------", message.content)


    input_message = HumanMessage(content=(message.content + "answer the questian with an australian slang"))


    response = app.invoke(
        {"messages": [input_message]},
    )
        
    await cl.Message(
        content=response["messages"][-1].content).send()
    
    print_messages(response)

    print("Answer content----------", response["messages"][-1].content)
    
