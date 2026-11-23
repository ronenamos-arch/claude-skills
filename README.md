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

## קרדיט

המרכז מבוסס על [מרכז הסקילים של קהילת בין קודש לקלוד](https://github.com/hiyabh/claude-skills),
שפורסם ברישיון MIT. תודה לקהילה על הבסיס.

## רישיון

MIT - לשימוש חופשי. מותר להעביר הלאה. פרטים בקובץ LICENSE.
