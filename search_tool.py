import os
import arabic_reshaper
from bidi.algorithm import get_display

def fix_arabic(text):
    # هذه الدالة تقوم بتعديل وترتيب الحروف العربية لتظهر صحيحة غير معكوسة
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

def load_database(filename="iveco_codes.txt"):
    codes_db = {}
    if not os.path.exists(filename):
        return codes_db
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or "|" not in line:
                continue
            code, description = line.split("|", 1)
            codes_db[code.strip().upper()] = description.strip()
    return codes_db

def main():
    print(fix_arabic("=" * 50))
    print(fix_arabic("      أداة البحث عن أعطال شاحنات إيفيكو      "))
    print(fix_arabic("=" * 50))
    
    database = load_database()
    if not database:
        print(fix_arabic("خطأ: ملف قاعدة البيانات غير موجود أو فارغ."))
        return
    
    print(fix_arabic(f"تم تحميل {len(database)} كود بنجاح.\n"))
    
    while True:
        query = input(fix_arabic("أدخل كود العطل (أو اكتب exit للخروج): ")).strip().upper()
        if query == 'EXIT':
            break
        if not query:
            continue
        if query in database:
            desc = fix_arabic(database[query])
            print(fix_arabic(f"\n[النتيجة] {query} : {desc}\n"))
        else:
            print(fix_arabic(f"\n[!] الكود '{query}' غير موجود.\n"))

if __name__ == "__main__":
    main()