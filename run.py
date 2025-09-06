from app import create_app, db
from config import Config

app = create_app()
app.config.from_object(Config)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ساخت دیتابیس و جدول‌ها در بار اول اجرا
    app.run(host="0.0.0.0", port=8080,debug=True)