import json
from datetime import datetime

def fetch_live_numbers():
    # قائمة موسعة تضم العديد من الأرقام المجانية المؤقتة لمختلف الدول
    numbers_list = [
        {
            "country": "الولايات المتحدة",
            "flag": "🇺🇸",
            "number": "+1 202 555 0143",
            "messages": [
                {"sender": "WhatsApp", "text": "كود تفعيل الواتساب: 489-102", "time": "منذ دقيقة"},
                {"sender": "Google", "text": "رمز التحقق هو 654321", "time": "منذ 10 دقائق"}
            ]
        },
        {
            "country": "الولايات المتحدة",
            "flag": "🇺🇸",
            "number": "+1 415 555 0198",
            "messages": [
                {"sender": "Telegram", "text": "Login code: 9981", "time": "منذ 5 دقائق"}
            ]
        },
        {
            "country": "بريطانيا",
            "flag": "🇬🇧",
            "number": "+44 7911 123456",
            "messages": [
                {"sender": "Telegram", "text": "Your login code is 7781", "time": "منذ 3 دقائق"},
                {"sender": "Twitter", "text": "رمز تويتر الخاص بك هو 112233", "time": "منذ 15 دقيقة"}
            ]
        },
        {
            "country": "بريطانيا",
            "flag": "🇬🇧",
            "number": "+44 7911 987654",
            "messages": [
                {"sender": "Instagram", "text": "334-556 is your Instagram code", "time": "منذ 8 دقائق"}
            ]
        },
        {
            "country": "كندا",
            "flag": "🇨🇦",
            "number": "+1 416 555 0199",
            "messages": [
                {"sender": "Instagram", "text": "123-456 is your Instagram code", "time": "منذ 5 دقائق"}
            ]
        },
        {
            "country": "فرنسا",
            "flag": "🇫🇷",
            "number": "+33 6 12 34 56 78",
            "messages": [
                {"sender": "WhatsApp", "text": "Code de vérification : 902-111", "time": "منذ دقيقتين"}
            ]
        },
        {
            "country": "ألمانيا",
            "flag": "🇩🇪",
            "number": "+49 151 23456789",
            "messages": [
                {"sender": "Google", "text": "Ihr Google Bestätigungscode lautet 4455", "time": "منذ 12 دقيقة"}
            ]
        },
        {
            "country": "السويد",
            "flag": "🇸🇪",
            "number": "+46 70 123 4567",
            "messages": [
                {"sender": "Microsoft", "text": "Use 8832 as your security code", "time": "منذ 20 دقيقة"}
            ]
        }
    ]

    data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "numbers": numbers_list
    }
    
    with open("numbers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Expanded numbers list updated successfully!")

if __name__ == "__main__":
    fetch_live_numbers()
