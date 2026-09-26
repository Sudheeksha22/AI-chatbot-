import streamlit as st

st.title("🤖 Welcome to AI Chatbot")

question = st.text_input("Enter your message")

if st.button("Generate"):
    if question == "":
        st.error("Please enter a message")
    else:
        st.success("Response generated successfully!")

        st.subheader(" Conversation")

        st.write("👤 You:", question)
        st.write("🤖 AI:", "Hello! I received your message.")