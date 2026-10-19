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
    # حساب وقت النهاية (5 ساعات = 5 * 60 * 60 ثانية = 18000 ثانية)
    start_time = time.time()
    duration = 5 * 60 * 60  # 5 ساعات بالثواني
    
    print("بدء تشغيل السكربت لمدة 5 ساعات...")

    while time.time() - start_time < duration:
        # 1. إرسال none
        send_command("none")
        time.sleep(10)
        
        # التحقق من انتهاء الوقت قبل إرسال الأمر الثاني
        if time.time() - start_time >= duration:
            break
            
        # 2. إرسال play
        send_command("play")
        time.sleep(10)

    print("انتهت مدة الـ 5 ساعات وتوقف السكربت.")
