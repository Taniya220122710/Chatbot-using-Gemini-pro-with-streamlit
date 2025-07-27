# 🤖 Chatbot using Gemini Pro with Streamlit

This project demonstrates a simple yet powerful AI-powered chatbot built using Google's **Gemini Pro model** and **Streamlit** for the web interface. It allows users to interact with the Gemini Pro language model in real-time via a friendly browser-based UI.



## 🚀 Features

- 🔮 **Gemini Pro integration** via Google's Generative AI API
- 💬 Real-time chatbot responses
- 🌐 Clean, interactive **Streamlit** UI
- 🔐 Secure API key management with `.env`
- 🧠 Intelligent and creative conversation capabilities


## 🖼️ Demo

<img src="<img width="1920" height="1020" alt="Screenshot 2025-07-27 221338" src="https://github.com/user-attachments/assets/cc889918-bcec-40ce-8c89-fe6317dd722c" />


## 🛠️ Tech Stack

| Component       | Description                                 |
|----------------|---------------------------------------------|
| 🧠 Gemini Pro   | Google's advanced LLM for text generation   |
| 🌐 Streamlit    | Python library to build the web interface   |
| 🔐 dotenv       | For storing API keys securely               |
| 🐍 Python 3.10+ | Programming language                        |


## 📝 How It Works

1. **User Input**: A user types a message into the chatbot.
2. **API Call**: The input is sent to Gemini Pro using `google.generativeai`.
3. **Model Response**: Gemini processes the prompt and returns a response.
4. **Display**: The response is displayed in the chat UI using Streamlit.

---

# Tech Stack and Tools Used

Tool	                              Purpose
Python	                     Core programming language
Streamlit	                   For building the web interface
Gemini Pro	                 Google’s large language model API
google-generativeai	         Python library to connect with Gemini Pro
dotenv	                     To securely load your API key from .env file

# Explanation of main.py

Step 1: Import Necessary Libraries

import streamlit as st

import google.generativeai as genai

from dotenv import load_dotenv

import os

 -> streamlit: Used to create the web interface (text input, display output).

 -> google.generativeai: Connects your app to Gemini Pro's language model.

 -> load_dotenv: Loads environment variables (like your API key) from a .env file.

 -> os: Lets you access environment variables and system paths.

 Step 2: Load API Key from .env

 load_dotenv()

genai.configure{os.getenv("GOOGLE_API_KEY"))

 -> load_dotenv(): Loads environment variables from the .env file.

 -> os.getenv("GOOGLE_API_KEY"): Reads your API key stored securely.

 -> genai.configure(...): Authenticates your code with the Gemini Pro service.

# .env file content should look like this:

GOOGLE_API_KEY=your_actual_gemini_api_key   (inside this is upload my api keys here)

Step 3: Initialize the Gemini Pro Model

model = genai.GenerativeModel("gemini-pro")
 This initializes the Gemini Pro model object. You will use this to send user prompts and receive AI-generated responses.

 Step 4: Set up the Streamlit UI
 
 -> st.title(...): Displays the title of the web page.

 -> st.text_input(...): Creates a text box where the user types their message.

Step 5: Handle User Input & Display Response

 -> When a user types something, it gets passed to generate_content().

 ->The Gemini Pro API processes the text and returns a response.

 -> The response is then displayed below using st.write().

 










