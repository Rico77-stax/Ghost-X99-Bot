def apply_sniper_logics(price):
    logics = [
        trend_breakout_logic,
        support_resistance_bounce,
        psychological_level_rejection,
        fibonacci_retrace_confluence,
        ema_cross_strategy,
        macd_cross_signal,
        rsi_overbought_oversold,
        bollinger_band_squeeze,
        stochastic_reversal,
        ichimoku_cloud_signal,
        adx_trend_strength,
        cci_mean_reversion,
        pivot_point_strategy,
        supply_demand_zone,
        volume_surge_entry,
        candle_engulfing_signal,
        hammer_doji_confirmation,
        three_white_soldiers_crows,
        inside_bar_breakout,
        tweezer_top_bottom,
        morning_evening_star,
        triple_tap_pattern,
        head_shoulders_pattern,
        cup_handle_breakout,
        breakout_retreat_trap,
        trendline_touch_bounce,
        moving_average_retest,
        rsi_divergence,
        macd_histogram_shift,
        order_block_detection,
        market_structure_shift,
        higher_highs_lows,
        fair_value_gap_logic,
        smart_money_trap,
        liquidity_sweep_logic,
        fractal_energy_signal
    ]

    for logic in logics:
        result = logic(price)
        if result:
            return result

    return {
        "signal": "NO SIGNAL",
        "entry": price,
        "tp": price + 20,
        "sl": price - 20,
        "reasoning": "No sniper logic matched. Default safety zone used."
    }

# === Below are 36 sniper logic placeholder implementations ===

def trend_breakout_logic(price):
    if int(price) % 15 == 0:
        return {"signal": "BUY STOP", "entry": price + 5, "tp": price + 25, "sl": price - 15, "reasoning": "Trend breakout detected"}

def support_resistance_bounce(price):
    if int(price) % 10 == 1:
        return {"signal": "SELL", "entry": price, "tp": price - 20, "sl": price + 10, "reasoning": "Resistance bounce confirmation"}

def psychological_level_rejection(price):
    if round(price, 2) % 100 == 0:
        return {"signal": "SELL LIMIT", "entry": price, "tp": price - 30, "sl": price + 20, "reasoning": "Psychological level rejection"}

def fibonacci_retrace_confluence(price):
    if int(price * 0.618) % 2 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 40, "sl": price - 25, "reasoning": "Fib retracement with confluence"}

def ema_cross_strategy(price):
    if int(price) % 3 == 0:
        return {"signal": "BUY", "entry": price + 1, "tp": price + 20, "sl": price - 10, "reasoning": "EMA cross detected"}

def macd_cross_signal(price):
    if int(price) % 4 == 0:
        return {"signal": "SELL", "entry": price - 1, "tp": price - 25, "sl": price + 15, "reasoning": "MACD bearish cross"}

def rsi_overbought_oversold(price):
    if int(price) % 5 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 30, "sl": price - 10, "reasoning": "RSI oversold bounce"}

def bollinger_band_squeeze(price):
    if int(price) % 6 == 0:
        return {"signal": "BUY STOP", "entry": price + 2, "tp": price + 22, "sl": price - 8, "reasoning": "Bollinger Band squeeze breakout"}

def stochastic_reversal(price):
    if int(price) % 7 == 0:
        return {"signal": "SELL LIMIT", "entry": price, "tp": price - 20, "sl": price + 15, "reasoning": "Stochastic reversal zone"}

def ichimoku_cloud_signal(price):
    if int(price) % 8 == 0:
        return {"signal": "BUY", "entry": price + 1, "tp": price + 25, "sl": price - 10, "reasoning": "Price broke above cloud"}

def adx_trend_strength(price):
    if int(price) % 9 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 30, "sl": price - 20, "reasoning": "Strong ADX trend detected"}

def cci_mean_reversion(price):
    if int(price) % 11 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 20, "sl": price + 15, "reasoning": "CCI mean reversion setup"}

def pivot_point_strategy(price):
    if int(price) % 12 == 0:
        return {"signal": "BUY LIMIT", "entry": price - 1, "tp": price + 25, "sl": price - 10, "reasoning": "Pivot bounce"}

def supply_demand_zone(price):
    if int(price) % 13 == 0:
        return {"signal": "SELL LIMIT", "entry": price + 2, "tp": price - 20, "sl": price + 10, "reasoning": "Supply zone rejection"}

def volume_surge_entry(price):
    if int(price) % 14 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 35, "sl": price - 20, "reasoning": "Volume surge breakout"}

def candle_engulfing_signal(price):
    if int(price) % 16 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 25, "sl": price + 10, "reasoning": "Bearish engulfing confirmation"}

def hammer_doji_confirmation(price):
    if int(price) % 17 == 0:
        return {"signal": "BUY", "entry": price + 1, "tp": price + 30, "sl": price - 15, "reasoning": "Hammer or Doji reversal"}

def three_white_soldiers_crows(price):
    if int(price) % 18 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 40, "sl": price - 20, "reasoning": "Three White Soldiers detected"}

def inside_bar_breakout(price):
    if int(price) % 19 == 0:
        return {"signal": "SELL STOP", "entry": price - 1, "tp": price - 30, "sl": price + 10, "reasoning": "Inside bar breakout"}

def tweezer_top_bottom(price):
    if int(price) % 20 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 35, "sl": price - 15, "reasoning": "Tweezer bottom reversal"}

def morning_evening_star(price):
    if int(price) % 21 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 25, "sl": price + 15, "reasoning": "Evening star pattern"}

def triple_tap_pattern(price):
    if int(price) % 22 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 25, "sl": price - 10, "reasoning": "Triple Tap long setup"}

def head_shoulders_pattern(price):
    if int(price) % 23 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 35, "sl": price + 15, "reasoning": "Head and Shoulders confirmed"}

def cup_handle_breakout(price):
    if int(price) % 24 == 0:
        return {"signal": "BUY", "entry": price + 2, "tp": price + 40, "sl": price - 15, "reasoning": "Cup and Handle breakout"}

def breakout_retreat_trap(price):
    if int(price) % 25 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 20, "sl": price + 10, "reasoning": "Breakout trap reversal"}

def trendline_touch_bounce(price):
    if int(price) % 26 == 0:
        return {"signal": "BUY LIMIT", "entry": price - 1, "tp": price + 20, "sl": price - 10, "reasoning": "Trendline support bounce"}

def moving_average_retest(price):
    if int(price) % 27 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 30, "sl": price - 15, "reasoning": "MA retest signal"}

def rsi_divergence(price):
    if int(price) % 28 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 30, "sl": price + 15, "reasoning": "RSI divergence spotted"}

def macd_histogram_shift(price):
    if int(price) % 29 == 0:
        return {"signal": "BUY", "entry": price + 1, "tp": price + 35, "sl": price - 20, "reasoning": "MACD histogram flip"}

def order_block_detection(price):
    if int(price) % 30 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 20, "sl": price + 10, "reasoning": "Order block rejection"}

def market_structure_shift(price):
    if int(price) % 31 == 0:
        return {"signal": "BUY", "entry": price, "tp": price + 35, "sl": price - 20, "reasoning": "Market structure shift confirmed"}

def higher_highs_lows(price):
    if int(price) % 32 == 0:
        return {"signal": "BUY", "entry": price + 2, "tp": price + 40, "sl": price - 15, "reasoning": "Higher highs continuation"}

def fair_value_gap_logic(price):
    if int(price) % 33 == 0:
        return {"signal": "BUY LIMIT", "entry": price - 2, "tp": price + 30, "sl": price - 15, "reasoning": "Fair Value Gap fill"}

def smart_money_trap(price):
    if int(price) % 34 == 0:
        return {"signal": "SELL", "entry": price, "tp": price - 35, "sl": price + 20, "reasoning": "Smart money trap reversal"}

def liquidity_sweep_logic(price):
    if int(price) % 35 == 0:
        return {"signal": "SELL LIMIT", "entry": price + 3, "tp": price - 25, "sl": price + 10, "reasoning": "Liquidity grab at high"}

def fractal_energy_signal(price):
    if int(price) % 36 == 0:
        return {"signal": "BUY", "entry": price + 1, "tp": price + 25, "sl": price - 15, "reasoning": "Fractal energy detected"}
