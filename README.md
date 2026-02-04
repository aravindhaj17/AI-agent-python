🤖 Python AI Agent from Scratch

A modular AI-powered research assistant built with LangChain and Anthropic Claude, designed with testability, CI, and clean architecture in mind.

This project demonstrates how to:

Build an AI agent using tools

Structure Python projects professionally

Add unit tests

Run CI with GitHub Actions

Keep code CI-safe and OS-independent

✨ Features

🔍 AI research agent powered by Claude (Anthropic)

🧩 Tool-based architecture (search, wiki, save)

🧪 Unit tests using pytest

🔁 CI pipeline with GitHub Actions

AI-agent-python/
│
├── main.py                 # Entry point for the AI agent
├── models.py               # Pydantic models (testable)
├── tools.py                # Custom agent tools
├── requirements.txt        # Runtime dependencies
├── requirements-dev.txt    # Dev + test dependencies
├── sample.env              # Environment variable template
│
├── tests/
│   └── test_models.py      # Unit tests
│
└── .github/
    └── workflows/
        └── test.yml        # CI pipeline
        
⚙️ Prerequisites

Python 3.10+

An Anthropic API key

Git

🚀 Installation

git clone https://github.com/aravindhaj17/AI-agent-python.git
cd AI-agent-python

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

▶️ Running the Agent

python main.py



🧼 Clean separation of models, logic, and tools

🐧 Linux-safe dependency handling for CI
