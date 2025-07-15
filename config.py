# === Quantum Ghost X99 – Vortex Sniper Configuration ===

# Telegram bot credentials (REAL values embedded)
BOT_TOKEN = "7974220853:AAE80t4o5-3UpZjRCaGDnnRcIMb0ZKbtXrk"
TELEGRAM_GROUP_ID = -1002824996503  # Ghost X99 sniper group

# Screenshot file types
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]

# Chart timeframe recognition (used for naming/image matching)
SUPPORTED_TIMEFRAMES = ["M15", "M30", "H1"]

# Core processing options
IMAGE_SAVE_PATH = "./"
OCR_LANG = "eng"

# Enable logic output annotation
DRAW_MARKUP = True

# Trade settings
DEFAULT_REWARD = 2  # R:R ratio
DEFAULT_RISK = 1
DEFAULT_SPREAD = 0.0  # Can be updated later if needed

# Fib + EMAs
USE_EMA_STRATEGY = True
USE_FIBONACCI = True
USE_SMART_MONEY = True
USE_LIQUIDITY_TRAPS = True
USE_RSI = True

# Screenshot signal logic settings
SCAN_FULL_SCREENSHOT = True
SIGNAL_ONLY_FROM_SCREENSHOT_END = True  # Core sniper rule
