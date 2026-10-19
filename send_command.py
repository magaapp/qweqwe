import time
import requests

# رابط قاعدة البيانات الخاصة بك
FIREBASE_URL = "https://test-b2fa9-default-rtdb.firebaseio.com/command.json"

def send_command(cmd):
    response = requests.put(FIREBASE_URL, json=cmd)
    if response.status_code == 200:
        print(f"تم إرسال الأمر بنجاح: {cmd}")
    else:
        print("فشل إرسال الأمر:", response.status_code)

if __name__ == "__main__":
    # تكرار إرسال الأمر 5 مرات (كل 10 ثوانٍ) ثم الانتهاء لكي لا يعلق الـ GitHub Actions
    for i in range(5):
        print(f"الإرسال رقم {i+1}...")
        send_command("play")
        if i < 4:  # لا تنتظر بعد المرة الأخيرة
            time.sleep(10)
            
    print("انتمى إرسال الأوامر بنجاح وتوقف الأكشن.")
