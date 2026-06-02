# ApnaSeat.in Automation Bot — Quick-Start Guide

## Files
```
apnaseat_bot.py   ← all Selenium logic (7 steps)
config.py         ← your settings (source, dest, date, weights …)
passenger.json    ← passenger details
requirements.txt  ← Python dependencies
```

## 1 — Install dependencies
```bash
pip install -r requirements.txt
```
Chrome + ChromeDriver must be installed and on your PATH.
`webdriver-manager` can auto-download ChromeDriver for you:
```python
# Add to top of apnaseat_bot.py if needed:
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opts)
```

## 2 — Configure your journey (config.py)
```python
SOURCE       = "SVP"
DESTINATION  = "DP"
TRAVEL_DATE  = "15-06-2026"   # DD-MM-YYYY
```

## 3 — Edit passenger details (passenger.json)
```json
{
  "name": "Roop Kumar",
  "age": "28",
  "gender": "Male",
  "phone": "9656565656",
  "email": "roop@example.com",
  "id_type": "Aadhaar",
  "id_number": "1234-5678-9012"
}
```

## 4 — Run
```bash
python apnaseat_bot.py
```

The bot will:
✅ Open Chrome and load apnaseat.in  
✅ Fill in source / destination / date  
✅ Click Search and wait for results  
✅ Scrape all available buses  
✅ Rank by fare → seats → departure time  
✅ Click the best bus to open the seat map  
✅ Pick the best available seat (window > front > lower > any)  
✅ Fill all passenger fields from passenger.json  
⛔ STOP — you review & pay manually  

## Ranking formula
```
score = (fare × -1) + (available_seats × 5) + departure_bonus
```
Weights are configurable in `config.py`.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| ChromeDriver version mismatch | Use `webdriver-manager` (see §1) |
| Autocomplete field not found | Inspect the page and add the right CSS selector to `_fill_autocomplete()` |
| Buses not scraped | Inspect element, update `card_selectors` in `scrape_buses()` |
| Seat map not opening | Inspect "View Seats" button and add its class to `open_seat_map()` |
| HEADLESS=True breaks | Set `HEADLESS=False` and watch it run |

Screenshots are saved in `screenshots/` after each step.
Logs are written to `apnaseat_bot.log`.

## Architecture overview
```
ApnaSeatBot (orchestrator)
 ├── BrowserManager   → anti-detection Chrome setup
 ├── SearchEngine     → Step 1-3  (open, form, scrape)
 ├── BusRanker        → Step 4    (score & rank)
 ├── SeatSelector     → Step 5-6  (seat map & pick)
 └── PassengerForm    → Step 7    (fill details)
```

## ⚠️ Ethical & Legal Note
This bot is for personal/educational use only.  
Always comply with ApnaSeat.in's Terms of Service.  
The bot intentionally does NOT auto-submit payment.
