# ============================================================
#  ApnaSeat.in — Bot Configuration
# ============================================================

# Journey details (edit these before running)
SOURCE       = "SVP"
DESTINATION  = "DP"
BOOKING_START_OFFSET = 1           # first journey date = today + this many days (1 = tomorrow)
BOOKING_DAY_COUNT    = 4           # number of consecutive days to process per cycle

# Passenger data file (relative or absolute path)
PASSENGER_FILE = "passenger.json"

# Browser settings
HEADLESS        = True             # True = invisible Chrome (required on Chrome 148.0.7778.179+)
SLOW_MO_MS      = 50              # ms between actions (0 = fastest)
PAGE_TIMEOUT_S  = 30              # max wait for any page load
ELEMENT_WAIT_S  = 15              # max wait for a single element

# Seat-selection preferences (in priority order)
SEAT_PREFERENCE = ["window", "front", "lower", "any"]

# Multi-seat random booking
SEAT_COUNT  = 4          # number of seats to book at once
SEAT_RANGE  = (1, 26)    # only pick seats whose label is numeric and in this range
SEAT_NUMBER = ""         # (legacy) force one specific seat; empty = random

# Ranking weights used to pick the best bus
WEIGHT_FARE            = -1       # lower fare → higher score
WEIGHT_SEATS           =  5       # more seats  → higher score
WEIGHT_DEPARTURE_BONUS =  10      # bonus for earlier departure

# Output / logging
LOG_FILE    = "apnaseat_bot.log"
SCREENSHOTS = True                # save screenshots on key steps
SCREENSHOT_DIR = "screenshots"
REPORT_DIR  = "reports"           # Excel booking reports
