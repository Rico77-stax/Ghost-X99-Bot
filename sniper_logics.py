import cv2 import numpy as np from utils.ema_utils import detect_ema_stack from utils.fib_utils import calculate_fibonacci_levels from utils.rsi_utils import detect_rsi_divergence from utils.structure_utils import detect_market_structure

def apply_sniper_logics(image, current_price): results = []

# 1. Detect market structure
structure = detect_market_structure(image)
if structure['trend'] == 'bullish':
    results.append("Market Structure: Bullish Trend")
elif structure['trend'] == 'bearish':
    results.append("Market Structure: Bearish Trend")

# 2. Break and retest zones
if structure['break_retest']:
    results.append("Break & Retest zone detected")

# 3. Order blocks detection (high volume reversal zones)
if structure['order_block']:
    results.append("Order Block zone identified")

# 4. Trap zones / Fakeout areas
if structure['trap_zone']:
    results.append("Trap zone detected (Fakeout)")

# 5. Liquidity sweeps (stop hunts near highs/lows)
if structure['liquidity_sweep']:
    results.append("Liquidity Sweep near major high/low")

# 6. Triple tap reversal pattern
if structure['triple_tap']:
    results.append("Triple Tap Reversal Pattern")

# 7. Psychological level interaction
if structure['psych_level']:
    results.append("Price reacting to psychological level")

# 8. EMA stack
ema_stack = detect_ema_stack(image)
if ema_stack == 'bullish':
    results.append("7 EMA Stack Bullish Alignment")
elif ema_stack == 'bearish':
    results.append("7 EMA Stack Bearish Alignment")

# 9. EMA rejections
if structure['ema_rejection']:
    results.append("Price rejection from EMA zone")

# 10. RSI divergence
if detect_rsi_divergence(image):
    results.append("RSI Divergence confirmed")

# 11. Trendline confirmation
if structure['trendline_touch']:
    results.append("Price bouncing off trendline")

# 12. Volume exhaustion zone
if structure['volume_exhaustion']:
    results.append("Volume Exhaustion Zone Identified")

# 13. Fibonacci sniper logic
fib = calculate_fibonacci_levels(image)
if fib['retracement'] in [61.8, 78.6]:
    results.append(f"Sniper Entry on Fibo Pullback {fib['retracement']}%")
if fib['extension']:
    results.append(f"TP Target: Fibo Extension {fib['extension']}")

# 14. Smart Money Concepts (SMC)
if structure['smc_confirmed']:
    results.append("SMC Entry Logic Triggered")

# 15–36: Extra sniper confluences (placeholders to expand modularly)
if structure['midline_flip']:
    results.append("Midline flip structure")
if structure['equal_highs_lows']:
    results.append("Equal Highs/Lows = Liquidity Pool")
if structure['m_pattern']:
    results.append("M-pattern reversal detected")
if structure['w_pattern']:
    results.append("W-pattern reversal detected")
if structure['ranged_consolidation']:
    results.append("Ranging structure pre-breakout")
if structure['wick_rejections']:
    results.append("Wick rejection confirmation")
if structure['imbalance_zone']:
    results.append("Imbalance zone detected")
if structure['price_action_zone']:
    results.append("High PA confluence zone")

# Add more logics here (36 total)

# Final decision placeholder (actual decision made in signal_engine)
return results

