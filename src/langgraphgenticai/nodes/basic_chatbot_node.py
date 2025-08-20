from src.langgraphgenticai.state import State

class BasicChatbotNode:
    """
    BasicChatbotNode is a simple chatbot node that can be used in a language graph.
    """

    def __init__(self, model):
        self.model = model

    def process(self,state:State)->dict:
        """
        Processes the state and returns a response from the chatbot model.
        """
        return {"messages": self.llm.invoke(state["messages"])}