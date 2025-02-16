import streamlit as st
import requests

# Backend API URL
API_URL = "http://localhost:8000/chat"

st.title("Customer Support Chatbot")
st.write("Welcome! How can I assist you today?")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    st.write(f"{message['role']}: {message['content']}")

# User input
user_input = st.text_input("Type your message here...", key="input")

if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "User", "content": user_input})
        print(user_input)
        # Send request to backend
        response = requests.post(API_URL, json={"message": user_input})
        print(response.json())
        if response.status_code == 200:
            bot_response = response.json()["response"]
            st.session_state.messages.append({"role": "Bot", "content": bot_response})
            st.rerun()  # Refresh the UI to display the new message
        else:
            st.error("Failed to get a response from the chatbot.")