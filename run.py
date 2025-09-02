from app import create_app
from config import Config

app = create_app()
app.config.from_object(Config)

if __name__ == "__main__":
    # اجرای پروژه در حالت debug برای توسعه
    app.run(host="0.0.0.0", port=8080, debug=True)