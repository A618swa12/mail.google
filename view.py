import sqlite3

# مسیر فایل دیتابیس شما
db_path = "database/logs.db"  # اگر فایل logs.db توی پوشه database هست

# اتصال به دیتابیس
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# انتخاب تمام داده‌ها از جدول user_log
cursor.execute("SELECT * FROM user_log")
rows = cursor.fetchall()

if rows:
    print(f"{'ID':<5} {'Username':<30} {'Password':<30}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<30} {row[2]:<30}")
else:
    print("هیچ رکوردی در دیتابیس وجود ندارد.")

# بستن اتصال
conn.close()