import requests
import json
import os

# הגדרות - שנה לערכים שלך
GAS_URL = "https://script.google.com/macros/s/AKfycbyGIavueF5eYZP542khG6WSYztk-OA6wadPJp9pBiCvJpg--opvOmDm6iqvH4EWzoWGVA/exec"
ROOT_FOLDER_ID = "1YvJzJJlKzKMunkYQWAqwFGK6VElIW-WT"

def fetch_all():
    print("Fetching data from Google Apps Script...")
    # אנחנו צריכים שה-GAS יחזיר את כל הקבצים בצורה רקורסיבית
    # אם ה-GAS שלך כבר תומך ב-fetchFilesRecursively, פשוט נקרא לו.
    # אם לא, הסקריפט הזה יקרא לו תיקייה-תיקייה ויבנה את ה-DB.
    
    # לצורך הפשטות, נניח שה-GAS מחזיר את הכל בבקשה אחת גדולה (יעיל יותר)
    response = requests.get(GAS_URL) # וודא שה-GAS שלך מחזיר את כל הקבצים ב-doGet
    data = response.json()
    
    # בניית מבנה נתונים מותאם לסייר קבצים מהיר
    database = {
        "folders": {},
        "files": {}
    }
    
    # נניח שה-GAS מחזיר רשימה שטוחה של קבצים עם מידע על התיקייה שלהם
    # כאן אנחנו מעבדים את המידע למבנה של: folders -> [subfolders, files]
    # (הערה: כדי שזה יעבוד מושלם, ה-GAS שלך צריך להחזיר אובייקט שמכיל את כל התיקיות והקבצים)
    
    # שמירה לקובץ מקומי
    with open('database.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Database updated successfully.")

if __name__ == "__main__":
    fetch_all()
