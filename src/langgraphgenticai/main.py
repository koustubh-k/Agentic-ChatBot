import streamlit as st
from BAsicChatbot.src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphgenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphgenticai.graph.graph_builder import GraphBuilder
from src.langgraphgenticai.ui.streamlitui.display_result import DisplayResultStreamlit



def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """

    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    user_message=st.chat_input("Enter your message:")
    
    if user_message:
        try:
            obj_llm_config=GroqLLM(user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: Failed to initialize the LLM model.")
                return
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except ValueError as ve:
                st.error(f"Error: {str(ve)}")
                return
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return