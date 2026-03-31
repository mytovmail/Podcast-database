import requests
import json
import sys
import time

# כתובת הסקריפט המעודכנת שלך
GAS_URL = "https://script.google.com/macros/s/AKfycbz3nayW_1lGLHc84KGnPcn_-o5lre0-txUOYkqQWOjenYVcfs7CTteNURzy9olm8pz77w/exec"

def fetch_all():
    try:
        print(f"מתחבר לסקריפט גוגל: {GAS_URL}")
        
        while True:
            # שליחת בקשה עם זמן המתנה (timeout) משמעותי
            response = requests.get(GAS_URL, timeout=300)
            response.raise_for_status() # בדיקה אם חזרה שגיאת HTTP
            
            data = response.json()
            
            # בדיקה האם הסקריפט עצר בגלל הגנת הזמן (4 דקות)
            if data.get("status") == "running":
                print("הסקריפט מתעכב ומבקש המשך סריקה (הגנת 4 דקות הופעלה)... ממתין 10 שניות וממשיך לסרוק.")
                time.sleep(10)
                continue # מבצע קריאה מחודשת לאותו הקישור
            
            # בדיקה בסיסית שהנתונים הגיעו במבנה הנכון בסיום
            if "folders" not in data or "files" not in data:
                print("שגיאה: מבנה הנתונים שהתקבל מגוגל אינו תקין")
                sys.exit(1)

            # שמירה לקובץ
            with open('database.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print("מסד הנתונים database.json עודכן בהצלחה!")
            break # סיום הלולאה
            
    except Exception as e:
        print(f"אירעה שגיאה בזמן העדכון: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_all()
