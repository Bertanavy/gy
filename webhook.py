from flask import Flask, request
import requests
import json

BOT_TOKEN = "7648772445:AAFQxEulPCcMeslH7BkNjmjKXlwmmraycfY"
CHAT_ID = -1002720022273

app = Flask("Webhook")

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, json=data)

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    content = request.get_json()
    if content:
        formatted = json.dumps(content, indent=2, ensure_ascii=False)
        send_to_telegram(f"📩 Сигнал получен:\n<pre>{formatted}</pre>")
    return "ok"

app.run(host="0.0.0.0", port=5001)
