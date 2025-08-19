Free OpenAI Chatbot (via RapidAPI)

An interactive ChatGPT-like chatbot built in Python using the ChatGPT-42 API on RapidAPI.
It lets you chat with GPT models (like gpt-4o-mini) directly from your terminal — without needing an OpenAI account.

🚀 Features

Interactive chat loop in terminal

Maintains conversation history (context-aware)

Works with gpt-4o-mini model via RapidAPI

Simple Python script (test.py)

📝 Prerequisites

Python 3.7+ installed

A free RapidAPI account

🔑 Step 1: Get a RapidAPI Key

Go to RapidAPI.

Sign up / log in.

Search for ChatGPT-42 API.

Subscribe to the free plan.

Copy your X-RapidAPI-Key from the "Code Snippets" tab.

💻 Step 2: Clone the Repo
git clone https://github.com/exall-fresh/free-openai-chatbot-rapidapi.git
cd free-openai-chatbot-rapidapi

📦 Step 3: Install Dependencies
pip install -r requirements.txt


(This will install requests.)

⚙️ Step 4: Export Your API Key

For security, don’t hardcode your key — store it in an environment variable.

Linux / macOS

export RAPIDAPI_KEY="your_key_here"


Windows (PowerShell)

setx RAPIDAPI_KEY "your_key_here"

▶️ Step 5: Run the Chatbot
python test.py


Example session:

You: hi
Bot: Hello! How are you today?
You: what's your name?
Bot: I'm an AI chatbot running on GPT-4o-mini via RapidAPI.


Type exit to quit.

📂 File Overview

test.py → Main Python chatbot script

requirements.txt → Required dependencies

README.md → Setup & usage guide

⚠️ Notes

Keep your RapidAPI key private (don’t commit it to GitHub).

Free RapidAPI plan has request limits.

This project is for learning/demo purposes.

📜 License

MIT License — free to use, modify, and share.
