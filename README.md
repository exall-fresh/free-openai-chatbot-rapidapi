# 🤖 Free OpenAI Chatbot (via RapidAPI)

Welcome to **Free OpenAI Chatbot RapidAPI Edition** 🎉  
This project allows you to connect to OpenAI's GPT models through **RapidAPI**, without needing a direct OpenAI account.  
You'll run a simple **Python chatbot** script (`test.py`) that talks to the AI right from your terminal. 🚀

---

## ✨ Features
- 🔑 No need to sign up directly with OpenAI – use RapidAPI instead  
- 💬 Chat with GPT models from your terminal  
- 🐍 Lightweight: only requires Python and `requests` library  
- 🌍 Works anywhere – just clone and run  

---

## 📝 Step 1: Register on RapidAPI

1. Go to [RapidAPI](https://rapidapi.com/) 🌐  
2. Click **Sign Up** (or **Login** if you already have an account)  
   - You can sign up with Google, GitHub, or email  
3. Once logged in, search for **ChatGPT API** in the search bar  
4. Choose a ChatGPT API provider and subscribe to the **free plan** (or another plan if you need more requests)  

---

## 🔑 Step 2: Get Your API Key

1. After subscribing, open the API's **Endpoints** page  
2. Look for the **x-rapidapi-key** value in the code snippets  
   - Copy it! This is your personal API key  
3. Replace the placeholder in `test.py` with your key:

```python
headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
    "x-rapidapi-key": "YOUR_API_KEY_HERE"  # replace this with your key
}
```

⚠️ **Important:** Keep this key private – don't share it or commit it to GitHub.

---

## 💻 Step 3: Clone and Setup the Project

Run the following commands in your terminal:

```bash
# Clone the repo
git clone https://github.com/exall-fresh/free-openai-chatbot-rapidapi.git

# Go inside the project folder
cd free-openai-chatbot-rapidapi

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install requests
```

---

## ⚙️ Step 4: Configure Your API Key

1. Open `test.py` in your favorite text editor
2. Find this line:
```python
"x-rapidapi-key": "YOUR_API_KEY_HERE"
```
3. Replace `YOUR_API_KEY_HERE` with the API key you copied from RapidAPI
4. Save the file

---

## ▶️ Step 5: Run the Chatbot

Run the script:

```bash
python test.py
```

**Example interaction:**

```
🤖 Free OpenAI Chatbot Started!
Type 'exit' to quit.

Enter your message: Hello AI!
AI: Hi there! How can I help you today? 🤖

Enter your message: What's the weather like?
AI: I don't have access to real-time weather data, but I can help you with general weather questions or suggest ways to check the weather in your area!

Enter your message: exit
👋 Goodbye!
```

Type `exit` to quit the chatbot.

---

## 📂 Project Structure

```
free-openai-chatbot-rapidapi/
├── test.py           # Main chatbot script
├── README.md         # This file
├── requirements.txt  # Python dependencies (optional)
└── .gitignore       # Git ignore file
```

---

## 🔧 Advanced Configuration

### Custom System Messages
You can modify the chatbot's personality by editing the system message in `test.py`:

```python
messages = [
    {"role": "system", "content": "You are a helpful and friendly AI assistant."},
    {"role": "user", "content": user_input}
]
```

### Model Selection
Some RapidAPI providers offer different models. Check your API documentation for available options and modify the request accordingly.

---

## 🐛 Troubleshooting

### Common Issues and Solutions:

**❌ `401 Unauthorized` Error**
- Check if your API key is correct and properly inserted
- Verify you're subscribed to the API on RapidAPI

**❌ `Quota Exceeded` Error**  
- You've hit your free plan limit
- Upgrade your plan on RapidAPI or wait for quota reset

**❌ `Module Not Found` Error**
- Make sure you installed requests: `pip install requests`
- If using a virtual environment, ensure it's activated

**❌ `Connection Error`**
- Check your internet connection
- Verify the API endpoint URL is correct

**❌ `JSON Decode Error`**
- The API might be returning an unexpected response
- Check if the API is working properly on RapidAPI's interface

---

## 📊 Usage Limits

Most free plans on RapidAPI have limits such as:
- **Requests per month:** 100-1000
- **Requests per minute:** 10-60  
- **Response length:** May be limited

Check your specific API provider's documentation for exact limits.

---

## 🚀 Next Steps

Want to enhance your chatbot? Here are some ideas:

- **💾 Save Conversations:** Add file logging to save chat history
- **🎨 Better UI:** Use libraries like `rich` for colored terminal output  
- **🌐 Web Interface:** Create a Flask/FastAPI web version
- **📱 GUI Version:** Build a desktop app with tkinter or PyQt
- **🧠 Memory:** Add conversation context memory
- **🔧 Commands:** Add special commands like `/help`, `/clear`, `/save`

---

## 💡 Contributing

Pull requests are welcome! 🎉  

To contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Ideas for contributions:**
- Better error handling
- Configuration file support
- Multiple API provider support
- Conversation export features
- Docker containerization

---

## 📋 Requirements

- **Python 3.6+**
- **requests** library
- **RapidAPI account** (free)
- **Internet connection**

---

## 🛡️ Security Notes

- Never commit your API keys to version control
- Use environment variables for production deployments:
  ```python
  import os
  api_key = os.getenv('RAPIDAPI_KEY')
  ```
- Consider using `.env` files with `python-dotenv` for local development

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and distribute.

```
MIT License

Copyright (c) 2025 Free OpenAI Chatbot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙋‍♀️ Support

Having issues? Here's how to get help:

1. **📖 Check this README** - Most common issues are covered here
2. **🐛 GitHub Issues** - Report bugs or request features  
3. **💬 Discussions** - Ask questions in GitHub Discussions
4. **📧 Contact** - Reach out to the maintainers

---

## ⭐ Show Your Support

If this project helped you, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** to contribute
- 📢 **Sharing** with friends who might find it useful
- 💬 **Leaving feedback** in the issues or discussions

---

**Happy Chatting! 🤖✨**
