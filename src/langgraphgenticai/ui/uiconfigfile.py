from configparser import ConfigParser

class Config:
    def __init__(self, config_file="uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_page_title(self):
        # Already correct, using a fallback
        return self.config.get("DEFAULT", "PAGE_TITLE", fallback="Default Page Title")

    def get_llm_options(self):
        # Added fallback to prevent errors if key is missing
        options_str = self.config.get("DEFAULT", "LLM_OPTIONS", fallback="Groq")
        return [opt.strip() for opt in options_str.split(',')]

    def get_usecase_options(self):
        # Added fallback
        options_str = self.config.get("DEFAULT", "USECASE_OPTIONS", fallback="Basic Chatbot")
        return [opt.strip() for opt in options_str.split(',')]

    def get_groq_model_options(self):
        # Added fallback
        options_str = self.config.get("DEFAULT", "GROQ_MODEL_OPTIONS", fallback="llama3-8b-8192")
        return [opt.strip() for opt in options_str.split(',')]
    