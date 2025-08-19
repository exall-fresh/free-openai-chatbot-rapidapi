import requests

url = "https://chatgpt-42.p.rapidapi.com/chat"

headers = {
    "Content-Type": "application/json",
    "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
    "x-rapidapi-key": "17a1edccffmsh259a705a79f17fap118bfbjsn3b63cd8c2a30"   # 🔑 replace with your actual key
}

# store conversation history
messages = []

while True:
    text = input("You: ")
    if text.lower() == "exit":
        break

    # append user message
    messages.append({"role": "user", "content": text})

    payload = {
        "messages": messages,
        "model": "gpt-4o-mini"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()

    try:
        reply = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        reply = "⚠️ Unexpected response: " + str(data)

    print("Bot:", reply)

    # append assistant reply to keep context
    messages.append({"role": "assistant", "content": reply})
