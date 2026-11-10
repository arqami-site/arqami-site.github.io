import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_live_numbers():
    numbers_list = []
    
    # يمكنك هنا إضافة استعلامات حقيقية أو جلب بيانات من مواقع الأرقام المؤقتة المتاحة
    # كمثال متطور، نقوم بتجهيز هيكل يدعم الدول الشهيرة للأرقام المؤقتة:
    try:
        # مثال لأرقام مؤقتة يتم جلبها وتحديث حالتها
        numbers_list.append({
            "country": "الولايات المتحدة",
            "flag": "🇺🇸",
            "number": "+1 202 555 0143",
            "messages": [
                {
                    "sender": "Verification",
                    "text": "Your verification code is 883921",
                    "time": "منذ دقيقة"
                }
            ]
        })
        numbers_list.append({
            "country": "بريطانيا",
            "flag": "🇬🇧",
            "number": "+44 7911 123456",
            "messages": [
                {
                    "sender": "WhatsApp",
                    "text": "Your WhatsApp code: 441-902",
                    "time": "منذ 3 دقائق"
                }
            ]
        })
        numbers_list.append({
            "country": "السعودية",
            "flag": "🇸🇦",
            "number": "+966 50 123 4567",
            "messages": [
                {
                    "sender": "Telegram",
                    "text": "Login code: 9942",
                    "time": "منذ 10 دقائق"
                }
            ]
        })
    except Exception as e:
        print(f"Error fetching numbers: {e}")

    return {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "numbers": numbers_list
    }

if __name__ == "__main__":
    data = fetch_live_numbers()
    with open("numbers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Scraper executed and numbers.json updated successfully!")
