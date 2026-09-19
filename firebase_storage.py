import os
import json
import firebase_admin
from firebase_admin import credentials, db

# ตรวจสอบว่ามี app โดน init ไปแล้วหรือยังเพื่อป้องกัน error รันซ้ำ
if not firebase_admin._apps:
    # 1. ดึงค่า JSON String จาก Environment Variable ที่ตั้งไว้ใน Render
    creds_env = os.environ.get("FIREBASE_CREDENTIALS")
    db_url = os.environ.get("FIREBASE_DATABASE_URL")

    if creds_env:
        # รันบน Server / Render: แปลง JSON string เป็น dict
        cred_dict = json.loads(creds_env)
        cred = credentials.Certificate(cred_dict)
    else:
        # รันบน Local: อ่านจากไฟล์ serviceAccountKey.json เดิมของคุณ
        cred = credentials.Certificate("serviceAccountKey.json")  # ใส่ path ไฟล์ local ของคุณ

    # 2. Initialize App
    firebase_admin.initialize_app(cred, {
        'databaseURL': db_url or 'https://fitcalc889-default-rtdb.firebaseio.com'
    })