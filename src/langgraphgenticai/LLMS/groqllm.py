import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls = user_controls_input
    def get_llm_model(self):
        try:
            groq_api_key=self.user_controls_input["GROQ_API_KEY"]
            selected_model=self.user_controls_input["selected_groq_model"]
            if groq_api_key=='' and os.get_env["GROQ_API_KEY"]=='':
                st.error("Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            
            llm=ChatGroq(api_key=groq_api_key, model=selected_model)

        except Exception as e:
            raise Exception(f"Error initializing Groq LLM: {str(e)}")
        return llm