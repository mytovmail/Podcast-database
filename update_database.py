import requests
import json
import sys

# כתובת הסקריפט המעודכנת שלך
GAS_URL = "https://script.google.com/macros/s/AKfycbyGIavueF5eYZP542khG6WSYztk-OA6wadPJp9pBiCvJpg--opvOmDm6iqvH4EWzoWGVA/exec"

def fetch_all():
    try:
        print(f"מתחבר לסקריפט גוגל: {GAS_URL}")
        # שליחת בקשה עם זמן המתנה (timeout) כדי למנוע תקיעה
        response = requests.get(GAS_URL, timeout=60)
        response.raise_for_status() # בדיקה אם חזרה שגיאת HTTP
        
        data = response.json()
        
        # בדיקה בסיסית שהנתונים הגיעו במבנה הנכון
        if "folders" not in data or "files" not in data:
            print("שגיאה: מבנה הנתונים שהתקבל מגוגל אינו תקין")
            sys.exit(1)

        # שמירה לקובץ
        with open('database.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("מסד הנתונים database.json עודכן בהצלחה!")
        
    except Exception as e:
        print(f"אירעה שגיאה בזמן העדכון: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_all()
