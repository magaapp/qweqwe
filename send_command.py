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
        # 1. إرسال none والانتظار لمدة 50 ثانية
        send_command("none")
        
        # الانتظار لمدة 50 ثانية مع التحقق من انتهاء الوقت الإجمالي كل ثانية
        wait_time = 50
        elapsed_wait = 0
        while elapsed_wait < wait_time:
            if time.time() - start_time >= duration:
                break
            time.sleep(1)
            elapsed_wait += 1
            
        # التحقق من انتهاء الوقت الإجمالي قبل الانتقال للخطوة التالية
        if time.time() - start_time >= duration:
            break
            
        # 2. إرسال play والانتظار لمدة 8 ثواني
        send_command("play")
        
        wait_time_play = 8
        elapsed_wait_play = 0
        while elapsed_wait_play < wait_time_play:
            if time.time() - start_time >= duration:
                break
            time.sleep(1)
            elapsed_wait_play += 1

    print("انتهت مدة الـ 5 ساعات وتوقف السكربت.")
