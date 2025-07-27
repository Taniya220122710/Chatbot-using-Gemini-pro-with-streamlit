import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Set Streamlit app configuration
st.set_page_config(
    page_title="Gemini ChatBot",
    page_icon="🤖",
    layout="centered"
)

# Initialize Gemini model
genai.configure(api_key=API_KEY)
gemini = genai.GenerativeModel("gemini-pro")

# Initialize chat session (only once)
if "chat" not in st.session_state:
    st.session_state.chat = gemini.start_chat(history=[])

# Function to map Gemini role to Streamlit role
def map_role(role):
    return "assistant" if role == "model" else role

# App title
st.title("🤖 Chat with Gemini-Pro")

# Show previous chat messages
for msg in st.session_state.chat.history:
    with st.chat_message(map_role(msg.role)):
        st.markdown(msg.parts[0].text)

# Accept user input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user's message
    st.chat_message("user").markdown(user_input)

    # Get response from Gemini
    reply = st.session_state.chat.send_message(user_input)

    # Display Gemini's response
    with st.chat_message("assistant"):
        st.markdown(reply.text)
