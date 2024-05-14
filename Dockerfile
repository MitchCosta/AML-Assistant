FROM python:3.11
RUN useradd -m -u 1000 user
#USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
WORKDIR $HOME/app
COPY --chown=user . $HOME/app
#COPY ./requirements.txt ~/app/requirements.txt
#RUN pip install -r requirements.txt
RUN pip install chainlit==0.7.700
RUN pip install python-dotenv==1.0.0
RUN pip install qdrant-client
RUN pip install langchain
RUN pip install langchain-community
RUN pip install langchain-openai
COPY . .

RUN chown -R user:user $HOME/app/Qdrant_db
USER user

CMD ["chainlit", "run", "app_one.py", "--port", "7860"]
