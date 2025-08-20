# File: app.py

import streamlit as st
from src.langgraphgenticai.main import load_langgraph_agenticai_app
from src.langgraphgenticai.ui.uiconfigfile import Config

# This MUST be the first Streamlit command
config = Config()
st.set_page_config(page_title="🤖 " + config.get_page_title(), layout="wide")

if __name__ == "__main__":
    load_langgraph_agenticai_app()