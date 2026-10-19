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
    # حلقة تكرار لإرسال الأمر بشكل متتالي كل 10 ثوانٍ
    while True:
        send_command("play")
        time.sleep(10)
