# Job Scan Agent

An intelligent LLM agent that can scan online job postings and provide detailed information with links. Built with LangChain and powered by Ollama, this agent uses the ReAct (Reasoning and Acting) framework to search for job opportunities and extract relevant details.

## Features

- **Intelligent Job Search**: Automatically searches for job postings based on your criteria
- **Detailed Information Extraction**: Provides comprehensive job details including requirements, location, and company information
- **Source Links**: Returns direct links to original job postings for easy access
- **Structured Output**: Uses Pydantic schemas for consistent, structured responses
- **Web Search Integration**: Leverages Tavily search for real-time job posting discovery

## Architecture

The agent is built using:
- **LangChain**: For agent orchestration and tool integration
- **Ollama**: Local LLM inference with Qwen3:14b model
- **Tavily Search**: For web search capabilities
- **ReAct Framework**: For reasoning and acting in a structured manner
- **Pydantic**: For data validation and structured outputs

## Installation

### Prerequisites

- Python 3.10 or higher
- Ollama installed and running
- Qwen3:14b model pulled in Ollama

### Setup

1. Clone the repository:
```bash
git clone https://github.com/tseste/job_scan_agent.git
cd job_scan_agent
```

2. Install dependencies using uv:
```bash
uv sync
```

3. Set up environment variables:
Create a `.env` file in the root directory and add your API keys:
```env
TAVILY_API_KEY=your_tavily_api_key_here
# optionally enable langsmith (requires langsmith accounts creation)
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=us_or_eu_langsmith_url
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=your_langsmith_project_name
```


4. Pull the required Ollama model:
```bash
ollama pull qwen3:14b

# a 12GB nvidia card could span the context window a little bit more. (default qwen3:14b 10GB)
ollama create -f ModelFile qwen3:14b-ctx
```

## Usage

### Basic Usage

Run the agent with a job search query:

```bash
python agent.py
```

The default example searches for AI engineer positions using LangChain in the Bay Area on LinkedIn.

### Streamlit Web Interface

For an interactive web interface, you can run the Streamlit app:

```bash
streamlit run app.py
```

This will launch a web interface where you can:
- Enter custom prompts interactively
- View structured responses with sources
- See conversation history
- Toggle raw JSON output for debugging

The web interface provides a user-friendly way to interact with the agent without modifying code.

## Configuration

### Model Configuration

The agent uses the Qwen3:14b model with the following configuration:
- Context window: 6144 tokens
- Model: qwen3:14b-ctx


## API Response Format

The agent returns structured responses with the following format:

```python
{
    "answer": "Detailed job information and analysis",
    "sources": [
        {
            "link": "https://example.com/job-posting-1"
        },
        {
            "link": "https://example.com/job-posting-2"
        }
    ]
}
```

## Troubleshooting

### Common Issues

1. **Ollama not running**: Ensure Ollama is installed and running ([ollama installation](https://ollama.com/download))
2. **Model not found**: Pull the required model with `ollama pull qwen3:14b`
3. **API key issues**: Verify your Tavily API key is correctly set in the `.env` file
4. **Memory issues**: The model requires significant RAM; ensure you have at least 12GB available
