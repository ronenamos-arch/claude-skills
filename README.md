# כל הסקילים של AI Finance Transformation

מרכז אחד לכל הסקילים ל-Claude Code - עם דף הסבר והתקנה בהדבקה אחת לכל סקיל.

**האתר:** https://ronenamos-arch.github.io/claude-skills/

**קורס קלוד AI MASTER עם רונן עמוס** (16 מודולים מעשיים, פרומפטים פיננסיים וסקילים):
https://www.ronenamoscpa.co.il/courses/sell-page

## התקנה מהירה (טרמינל)

```bash
curl -fsSL https://ronenamos-arch.github.io/claude-skills/install.sh | bash -s -- debug test-loop
```

להתקנת **כל** הסקילים:

```bash
curl -fsSL https://ronenamos-arch.github.io/claude-skills/install.sh | bash -s -- all
```

הסקריפט לא דורס סקיל קיים באותו שם.

## מבנה

| נתיב | מה יש שם |
|---|---|
| `src/<name>/` | קוד המקור של כל סקיל (מה שמותקן ב-`~/.claude/skills/<name>`) |
| `content/<name>.json` | תוכן דף ההסבר בעברית |
| `guides_src/<name>.html` | דפי מדריך (גוף הדף, ולצדו קבצי טקסט לפרומפטים). רשומים תחת `guides` ב-`catalog.json` |
| `catalog.json` | הכרטיסים המומלצים, כרטיס הקורס והמדריכים |
| `build/` | סקריפטי הבנייה (Python, בלי תלויות) |
| `skills/`, `dl/`, `index.html` | **נוצרים ע"י הבנייה** - לא לערוך ידנית |

## הוספת סקיל

מעתיקים את התיקייה ל-`src/<name>/`, כותבים `content/<name>.json` (ראו דוגמה קיימת),
מריצים `python build/og_images.py` (תמונת השיתוף לווטסאפ, 1200x630 - צריך Pillow
ו-python-bidi), אחר כך `python build/build.py`, ודוחפים. גם כששמים כותרת, תיאור או
אייקון חדשים - מריצים שוב את `og_images.py`: לתמונה מתקבל שם קובץ חדש, והרשתות לא
מציגות את הישנה מהזיכרון.

## סקילים חדשים: ראיית חשבון ישראלית ו-ICM

נוספו 14 סקילים מהמאגר [AI-Finance-Transformation](https://github.com/ronenamos-arch/AI-Finance-Transformation) וסקיל [ICM Architect](https://github.com/ronenamos-arch/icm-architect). לכל אחד דף הסבר בעברית, חבילת התקנה וקובצי מקור מלאים. בסך הכול: 44 סקילים.

סקילי החשבונאות הם כלי עזר. קובצי המקור הועתקו כפי שהם ולא עברו אימות מקצועי של שיעורים, ספים או הוראות דין. יש לאמת מידע עדכני ולבדוק כל פלט לפני דיווח או פעולה כספית.

- [חשבונית ירוקה (Morning)](https://ronenamos-arch.github.io/claude-skills/skills/green-invoice/): חיבור ל-API של Morning לניהול חשבוניות, קבלות, לקוחות ותהליכי מסמכים.
- [מעקב כספי ישראלי ב-Google Sheets](https://ronenamos-arch.github.io/claude-skills/skills/gws-israeli-business-sheets/): בניית גיליונות הכנסות והוצאות בשקלים, סיכומי מע״מ וגיבויים באמצעות Google Workspace CLI.
- [המרת נתונים מחשבשבת](https://ronenamos-arch.github.io/claude-skills/skills/hashavshevet-data-tools/): העברת פקודות יומן, כרטסות ומאזנים בין יצואי חשבשבת לבין CSV, Excel ו-JSON.
- [סידור חשבוניות לרואה החשבון](https://ronenamos-arch.github.io/claude-skills/skills/il-invoice-organizer/): ארגון חשבוניות בעברית, חילוץ נתונים וסיווג הוצאות לקראת העברה להנהלת החשבונות.
- [ניתוח דוחות שנתיים ישראליים](https://ronenamos-arch.github.io/claude-skills/skills/israeli-annual-reports/): קריאה וניתוח של דוחות תקופתיים, דיווחי מאי״ה ומונחים חשבונאיים בעברית.
- [התאמות בנקים בישראל](https://ronenamos-arch.github.io/claude-skills/skills/israeli-bank-reconciliation/): התאמת תנועות בנק לחשבוניות וקבלות, זיהוי פערים והכנת דוח התאמה.
- [טיוטות פקודות יומן](https://ronenamos-arch.github.io/claude-skills/skills/israeli-bookkeeping-automation/): בניית פקודות יומן לעסקאות נפוצות בישראל, כולל מע״מ, שכר, פחת והכרה בהכנסה.
- [חשבוניות אלקטרוניות בישראל](https://ronenamos-arch.github.io/claude-skills/skills/israeli-e-invoice/): הכנת ובדיקת מבני חשבוניות אלקטרוניות ועבודה עם דרישות מספרי הקצאה.
- [סיווג הוצאות עסקיות](https://ronenamos-arch.github.io/claude-skills/skills/israeli-expense-categorizer/): מיון הוצאות לקטגוריות חשבונאיות והכנת רשימה לבדיקת הכרה לצורכי מס ומע״מ.
- [הכנת דוחות כספיים](https://ronenamos-arch.github.io/claude-skills/skills/israeli-financial-reports/): הכנת טיוטות רווח והפסד, מאזן, מאזן בוחן ותזרים מזומנים מנתוני העסק.
- [חישובי שכר בישראל](https://ronenamos-arch.github.io/claude-skills/skills/israeli-payroll-calculator/): הערכת ברוטו-נטו, ניכויי עובד, הפרשות ועלות מעסיק לפי נתוני העובד.
- [חילוץ נתונים מקבלות](https://ronenamos-arch.github.io/claude-skills/skills/israeli-receipt-scanner/): קריאת קבלות וחשבוניות ישראליות והמרת פרטי העסקה לטבלת נתונים או JSON.
- [בניית חיבור חשבוניות לשע״מ](https://ronenamos-arch.github.io/claude-skills/skills/israeli-shaam-e-invoice-builder/): תכנון אינטגרציה לשע״מ: אימות, בניית JSON, בדיקות וזרימת בקשת מספר הקצאה.
- [הכנה ובדיקה של דוחות מע״מ](https://ronenamos-arch.github.io/claude-skills/skills/israeli-vat-reporting/): חישוב וריכוז מע״מ עסקאות ותשומות ובדיקת נתונים לקראת דיווח תקופתי.
- [ארכיטקט סביבת עבודה ICM](https://ronenamos-arch.github.io/claude-skills/skills/icm-architect/): הפיכת תהליך או אוסף ידע לסביבת תיקיות שקופה, עם שלבים, הקשר ובדיקות.

## סקילים חדשים: Pivot, מסרטון לסקיל ומסמכים בעברית

נוספו שלושה סקילים, ולכל אחד דף הסבר בעברית, חבילת התקנה וקובצי מקור. בסך הכול: 47 סקילים.

- [דוחות Pivot מטבלאות גולמיות](https://ronenamos-arch.github.io/claude-skills/skills/pivot-excel/): הופך טבלת נתונים לדוח Pivot ניתן לרענון, עם דוגמה בעברית.
- [מסרטון הדרכה לסקיל](https://ronenamos-arch.github.io/claude-skills/skills/video-to-skill/): הופך סרטון הדרכה או תמלול לסקיל שאפשר להפעיל שוב.
- [מחולל מסמכים בעברית](https://ronenamos-arch.github.io/claude-skills/skills/hebrew-document-generator/): מסמכי Word, PDF ו-PowerPoint בעברית עם כיווניות נכונה.

## סקיל חדש: tldr

נוסף סקיל אחד, עם דף הסבר בעברית, חבילת התקנה ודוגמה. בסך הכול: 49 סקילים.

- [שורה תחתונה של עשר שניות בכל תשובה](https://ronenamos-arch.github.io/claude-skills/skills/tldr/): התשובה המלאה נשארת כמו שהיא, ואחריה קו מפריד וסיכום קצר של ההחלטות.

## קרדיט

המרכז מבוסס על [מרכז הסקילים של קהילת בין קודש לקלוד](https://github.com/hiyabh/claude-skills),
שפורסם ברישיון MIT. תודה לקהילה על הבסיס.

סקילי החשבונאות: Copyright (c) 2026 Skills IL (Yootech), MIT.
ICM Architect: Copyright (c) 2026 Jake Van Clief, MIT.
מחולל מסמכים בעברית: Copyright (c) 2026 Skills IL (Yootech), MIT.
Astryx: Copyright (c) 2026 Meta Platforms, Inc., MIT.
רישיונות המקור כלולים בכל תיקיית סקיל ובחבילת ההורדה.

## רישיון

MIT - לשימוש חופשי. מותר להעביר הלאה. פרטים בקובץ LICENSE.
