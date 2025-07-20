import cv2
import numpy as np

def apply_all_sniper_logics(img):
    resized = cv2.resize(img, (640, 480))
    logic_results = []

    # 1. Order Blocks
    if detect_order_block(resized):
        logic_results.append("OB")

    # 2. Fair Value Gaps
    if detect_fvg(resized):
        logic_results.append("FVG")

    # 3. Liquidity Grab
    if detect_liquidity_grab(resized):
        logic_results.append("Liquidity Grab")

    # 4. Breaker Blocks
    if detect_breaker_block(resized):
        logic_results.append("Breaker Block")

    # 5. Trendline Breakout
    if detect_trendline_break(resized):
        logic_results.append("Trendline Break")

    # 6. Double Top/Bottom
    if detect_double_top_bottom(resized):
        logic_results.append("Double Top/Bottom")

    # 7. EMA Cross
    if detect_ema_cross(resized):
        logic_results.append("EMA Cross")

    # 8. Candlestick Pattern
    if detect_candlestick_pattern(resized):
        logic_results.append("Candle Pattern")

    # 9. Rejection Wicks
    if detect_rejection_wick(resized):
        logic_results.append("Rejection Wick")

    # 10. Inside Bar Setup
    if detect_inside_bar(resized):
        logic_results.append("Inside Bar")

    # 11. Break of Structure (BOS)
    if detect_bos(resized):
        logic_results.append("BOS")

    # 12. Change of Character (CHOCH)
    if detect_choch(resized):
        logic_results.append("CHOCH")

    # 13. Fibonacci Confluence
    if detect_fibonacci_zone(resized):
        logic_results.append("Fibo Confluence")

    # 14. Institutional Candle
    if detect_institutional_candle(resized):
        logic_results.append("Institutional Candle")

    # 15. Imbalance Zone
    if detect_imbalance(resized):
        logic_results.append("Imbalance")

    # 16. Supply & Demand
    if detect_supply_demand(resized):
        logic_results.append("S/D Zone")

    # 17. VWAP Bounce
    if detect_vwap_bounce(resized):
        logic_results.append("VWAP")

    # 18. Trend Channel
    if detect_trend_channel(resized):
        logic_results.append("Trend Channel")

    # 19. RSI Oversold/Overbought
    if detect_rsi_extreme(resized):
        logic_results.append("RSI Signal")

    # 20. MACD Divergence
    if detect_macd_divergence(resized):
        logic_results.append("MACD Divergence")

    # 21. Market Structure Shift
    if detect_market_structure_shift(resized):
        logic_results.append("Structure Shift")

    # 22. POI Rejection
    if detect_poi_reject(resized):
        logic_results.append("POI Rejection")

    # 23. Breakout Candle
    if detect_breakout_candle(resized):
        logic_results.append("Breakout Candle")

    # 24. Price Compression
    if detect_price_compression(resized):
        logic_results.append("Price Compression")

    # 25. Stop Hunt
    if detect_stop_hunt(resized):
        logic_results.append("Stop Hunt")

    # 26. Order Flow Shift
    if detect_order_flow_shift(resized):
        logic_results.append("Order Flow Shift")

    # 27. Round Number Trap
    if detect_round_number_trap(resized):
        logic_results.append("Round Number Trap")

    # 28. Session Timing Filter
    if detect_session_timing(resized):
        logic_results.append("Session Filter")

    # 29. Spread Spike
    if detect_spread_spike(resized):
        logic_results.append("Spread Spike")

    # 30. W Pattern
    if detect_w_pattern(resized):
        logic_results.append("W Pattern")

    # 31. M Pattern
    if detect_m_pattern(resized):
        logic_results.append("M Pattern")

    # 32. Range Breakout
    if detect_range_breakout(resized):
        logic_results.append("Range Break")

    # 33. OB+FVG Combo
    if "OB" in logic_results and "FVG" in logic_results:
        logic_results.append("OB+FVG Combo")

    # 34. BOS+CHOCH Combo
    if "BOS" in logic_results and "CHOCH" in logic_results:
        logic_results.append("Structure Combo")

    # 35. Liquidity Sweep + OB
    if "Liquidity Grab" in logic_results and "OB" in logic_results:
        logic_results.append("Liquidity + OB")

    # 36. Safe + Aggressive + Scalping Mode Mix Logic (based on config)
    from config import SAFE_MODE, AGGRESSIVE_MODE, SCALPING_MODE
    if SAFE_MODE:
        logic_results.append("Safe Mode Logic")
    if AGGRESSIVE_MODE:
        logic_results.append("Aggressive Mode Logic")
    if SCALPING_MODE:
        logic_results.append("Scalping Mode Logic")

    if logic_results:
        return f"📈 *Trade Signal Detected*\nType: {decide_entry_type(logic_results)}\nTP: 100 pips\nSL: 35 pips\nReason: {' + '.join(logic_results)}\n\n🧠 Analysis Done By Ghost X99"
    else:
        return None

# Stub pattern matchers — you can replace with real OpenCV detection
def detect_order_block(img): return avg_brightness(img) > 110
def detect_fvg(img): return edge_density(img) > 0.15
def detect_liquidity_grab(img): return brightness_variation(img) > 30
def detect_breaker_block(img): return color_zone_check(img, 100, 180)
def detect_trendline_break(img): return edge_count(img) > 120
def detect_double_top_bottom(img): return True
def detect_ema_cross(img): return False
def detect_candlestick_pattern(img): return avg_brightness(img) < 90
def detect_rejection_wick(img): return wick_shadow_check(img)
def detect_inside_bar(img): return True
def detect_bos(img): return True
def detect_choch(img): return True
def detect_fibonacci_zone(img): return True
def detect_institutional_candle(img): return True
def detect_imbalance(img): return True
def detect_supply_demand(img): return True
def detect_vwap_bounce(img): return True
def detect_trend_channel(img): return True
def detect_rsi_extreme(img): return True
def detect_macd_divergence(img): return True
def detect_market_structure_shift(img): return True
def detect_poi_reject(img): return True
def detect_breakout_candle(img): return True
def detect_price_compression(img): return True
def detect_stop_hunt(img): return True
def detect_order_flow_shift(img): return True
def detect_round_number_trap(img): return True
def detect_session_timing(img): return True
def detect_spread_spike(img): return True
def detect_w_pattern(img): return True
def detect_m_pattern(img): return True
def detect_range_breakout(img): return True

# === Helper Logic ===
def avg_brightness(img):
    return np.mean(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

def edge_density(img):
    edges = cv2.Canny(img, 100, 200)
    return np.count_nonzero(edges) / edges.size

def brightness_variation(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return np.std(gray)

def edge_count(img):
    edges = cv2.Canny(img, 100, 200)
    return np.count_nonzero(edges)

def color_zone_check(img, min_val, max_val):
    avg = np.mean(img)
    return min_val < avg < max_val

def wick_shadow_check(img):
    return True  # Replace with vertical wick detection logic

def decide_entry_type(logics):
    if "OB+FVG Combo" in logics or "Structure Combo" in logics:
        return "Buy Limit"
    if "Liquidity + OB" in logics:
        return "Sell Stop"
    if "RSI Signal" in logics:
        return "Scalp Buy"
    if "MACD Divergence" in logics:
        return "Buy"
    return "Buy" if avg_brightness(img) > 100 else "Sell"
