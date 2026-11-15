import json, re, requests
from datetime import datetime

# هذا الملف يشتغل في الخلفية فقط - الزائر ما يشوفه
# يجيب الأرقام الحقيقية ويحفظها في numbers.json
# الزائر يشوف numbers.json فقط، ما يعرف المصدر

def fetch_real_numbers():
    numbers_list = []
    try:
        # نجيب الصفحة الأصلية بالخلفية (الزائر ما يشوف هذا الرابط)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        r = requests.get("https://getfreesmsnumber.com/", headers=headers, timeout=20)
        html = r.text

        # نستخرج الأرقام الحقيقية من الصفحة
        found = re.findall(r"\+(?:1\s?\d{3}[\-\s]?\d{3}[\-\s]?\d{4}|31\s?\d{9,10}|358\s?\d{9,10}|44\s?\d{10})", html)
        seen = set()
        for num in found:
            clean = re.sub(r"\s+", " ", num).strip()
            # نتجاهل الأرقام المقنعة *** والأرقام الوهمية 555
            if "***" in clean or "555" in clean:
                continue
            if clean in seen:
                continue
            seen.add(clean)
            if clean.startswith("+1"):
                country, flag = "الولايات المتحدة", "🇺🇸"
            elif clean.startswith("+31"):
                country, flag = "هولندا", "🇳🇱"
            elif clean.startswith("+358"):
                country, flag = "فنلندا", "🇫🇮"
            elif clean.startswith("+44"):
                country, flag = "بريطانيا", "🇬🇧"
            else:
                country, flag = "دولي", "🌍"
            numbers_list.append({
                "country": country,
                "flag": flag,
                "number": clean,
                "messages": [
                    {"sender": "System", "text": "اضغط على الرقم لعرض الرسائل الحالية", "time": "الآن"}
                ]
            })
        print(f"تم جلب {len(numbers_list)} رقم حقيقي")
    except Exception as e:
        print(f"فشل الجلب: {e}")
        numbers_list = [
            {"country": "الولايات المتحدة", "flag": "🇺🇸", "number": "+1 407-544-9125", "messages": [{"sender": "System", "text": "اضغط لعرض الرسائل", "time": "الآن"}]},
            {"country": "الولايات المتحدة", "flag": "🇺🇸", "number": "+1 413-278-4571", "messages": [{"sender": "System", "text": "اضغط لعرض الرسائل", "time": "الآن"}]},
            {"country": "هولندا", "flag": "🇳🇱", "number": "+31 97058029582", "messages": [{"sender": "System", "text": "اضغط لعرض الرسائل", "time": "الآن"}]},
            {"country": "فنلندا", "flag": "🇫🇮", "number": "+358 4573989692", "messages": [{"sender": "System", "text": "اضغط لعرض الرسائل", "time": "الآن"}]},
        ]

    data = {"last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "numbers": numbers_list}
    with open("numbers.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("تم تحديث numbers.json بنجاح!")

if __name__ == "__main__":
    fetch_real_numbers()
