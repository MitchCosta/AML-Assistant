

<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>


## <h1 align="center" id="heading">Welcome to AML Compliance Assistante!!</h1>

For a step-by-step YouTube video walkthrough, watch this! [Deploying Chainlit app on Hugging Face](https://www.youtube.com/live/pRbbZcL0NMI?si=NAYhMZ_suAY84f06&t=2119)

![Alt text](Data/aml_compliance_assistant.png "Title")

# Overview:

The AML Compliance Assistant is a tool designed to aid individuals working in the field of Anti-Money Laundering (AML) and Counter-Terrorism Financing (CTF), particularly those navigating the complexities of the Australian AML/CTF Act of 2006.

# Purpose:


The primary goal of the AML Compliance Assistant is to support junior lawyers or individuals new to AML by providing a resource that simplifies and clarifies the intricate aspects of AML legislation.

# Key Features:

Educational Tool: The assistant serves as an educational resource, explaining the fundamental concepts of AML and the specifics of Australian legislation.
Document Navigation: It helps users navigate through complex legislative documents, including amendments and references to other acts.
Simplification of Legal Language: The tool translates complex legal language into more understandable terms, making it easier for users to comprehend and apply the regulations.


> If you need an introduction to `git`, or information on how to set up API keys for the tools we'll be using in this repository - check out our [Interactive Dev Environment for LLM Development](https://github.com/AI-Maker-Space/Interactive-Dev-Environment-for-LLM-Development/tree/main) which has everything you'd need to get started in this repository!



<details>
  <summary>🐳 Containerizing our App</summary>

1. Let's build the Docker image. We'll tag our image as `llm-app` using the `-t` parameter. The `.` at the end means we want all of the files in our current directory to be added to our image.
     
     ``` bash
     docker build -t llm-app .
     ```

2. Run and test the Docker image locally using the `run` command. The `-p`parameter connects our **host port #** to the left of the `:` to our **container port #** on the right.
    
     ``` bash
     docker run -p 7860:7860 llm-app
     ```

3. Visit http://localhost:7860 in your browser to see if the app runs correctly.

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/2c764f25-09a0-431b-8d28-32246e0ca1b7"> 
</p>

Great! Time to ship!
</details>


<details>
  <summary>🚀 Deploying Your First LLM App</summary>

1. Let's create a new Huggingface Space. Navigate to [Huggingface](https://huggingface.co) and click on your profile picture on the top right. Then click on `New Space`.

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/f0656408-28b8-4876-9887-8f0c4b882bae"> 
</p>

2. Setup your space as shown below:
   
- Owner: Your username
- Space Name: `llm-app`
- License: `Openrail`
- Select the Space SDK: `Docker`
- Docker Template: `Blank`
- Space Hardware: `CPU basic - 2 vCPU - 16 GB - Free`
- Repo type: `Public`

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/8f16afd1-6b46-4d9f-b642-8fefe355c5c9"> 
</p>

3. You should see something like this. We're now ready to send our files to our Huggingface Space. After cloning, move your files to this repo and push it along with your docker file. You DO NOT need to create a Dockerfile. Make sure NOT TO push your `.env` file. This should automatically be ignored.

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/cbf366e2-7613-4223-932a-72c67a73f9c6"> 
</p>

4. After pushing all files, navigate to the settings in the top right to add your OpenAI API key.

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/a1123a6f-abdd-4f76-bea4-39acf9928762"> 
</p>

5. Scroll down to `Variables and secrets` and click on `New secret` on the top right.

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/a8a4a25d-752b-4036-b572-93381370c2db"> 
</p>

6. Set the name to `OPENAI_API_KEY` and add your OpenAI key under `Value`. Click save.

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/0a897538-1779-48ff-bcb4-486af30f7a14"> 
</p>

7. To ensure your key is being used, we recommend you `Restart this Space`.

<p align = "center" draggable=”false”>
<img src="https://github.com/AI-Maker-Space/LLMOps-Dev-101/assets/37101144/fb1d83af-6ebe-4676-8bf5-b6d88f07c583"> 
</p>

8. Congratulations! You just deployed your first LLM! 🚀🚀🚀 Get on linkedin and post your results and experience! Make sure to tag us at #AIMakerspace !

Here's a template to get your post started!

```
🚀🎉 Exciting News! 🎉🚀

🏗️ Today, I'm thrilled to announce that I've successfully built and shipped my first-ever LLM using the powerful combination of Chainlit, Docker, and the OpenAI API! 🖥️

Check it out 👇
[LINK TO APP]

A big shoutout to the @**AI Makerspace** for all making this possible. Couldn't have done it without the incredible community there. 🤗🙏

Looking forward to building with the community! 🙌✨ Here's to many more creations ahead! 🥂🎉

Who else is diving into the world of AI? Let's connect! 🌐💡

#FirstLLM #Chainlit #Docker #OpenAI #AIMakerspace
```

</details>

<p></p>
