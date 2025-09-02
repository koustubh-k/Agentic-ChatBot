### End to End LangGraph Chat App
# LangGraph Agentic AI Application

A comprehensive application demonstrating Agentic AI capabilities using LangGraph with multiple use cases including basic chatbot, web-enhanced chatbot, and AI news summarization.

## Features

- 🤖 Basic Chatbot: Simple conversational AI
- 🌐 Web-Enhanced Chatbot: Chatbot with web search capabilities
- 📰 AI News Explorer: Fetch and summarize AI news (Daily/Weekly/Monthly)
- 🎨 Streamlit UI: User-friendly interface

## Tech Stack

- **LangGraph**: For building stateful AI agent workflows
- **Groq LLM**: Large Language Model integration
- **Streamlit**: Web interface
- **Tavily**: Web search integration
- **Python**: Core programming language

## Prerequisites

- Python 3.8+
- API Keys:
  - Groq API key from [console.groq.com](https://console.groq.com/keys)
  - Tavily API key from [app.tavily.com](https://app.tavily.com/home)

## Installation

1. Clone the repository:
```sh
git clone [repository-url]
cd AINEWSAgentic
```

2. Create and activate virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

1. Run the application:
```sh
streamlit run app.py
```

2. In the Streamlit UI:
   - Select LLM (Currently supports Groq)
   - Enter your API keys
   - Choose a use case:
     - Basic Chatbot
     - Chatbot With Web
     - AI News

3. For AI News:
   - Select timeframe (Daily/Weekly/Monthly)
   - Click "Fetch Latest AI News"
   - View summarized news in markdown format

## Project Structure

```
├── AINews/                 # AI news summaries storage
├── src/
│   └── langgraphagenticai/
│       ├── LLMS/          # LLM configurations
│       ├── graph/         # Graph builder logic
│       ├── nodes/         # Agent nodes
│       ├── state/         # State management
│       ├── tools/         # External tool integrations
│       └── ui/            # UI components
├── app.py                 # Main application entry
├── requirements.txt       # Dependencies
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
