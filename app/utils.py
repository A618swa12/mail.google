def log_user_action(username, password, ip):
    print(f"[LOG] User: {username}, Password: {password}, IP: {ip}")

def send_telegram_message(bot_token: str, chat_id: str, message: str):
    import requests
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        requests.post(url, data=data)
    except Exception as e:
        print(f"Telegram message failed: {e}")