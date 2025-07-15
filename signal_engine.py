import pandas as pd import numpy as np from sniper_logics import *

def analyze_signals(df): results = []

close = df['close']
open_ = df['open']
high = df['high']
low = df['low']
volume = df['volume']

price = close.iloc[-1]

results.append(logic_ema_cross(close))
results.append(logic_rsi_extremes(close))
results.append(logic_macd_cross(close))
results.append(logic_bollinger_bounce(close))
results.append(logic_stochastic_cross(close))
results.append(logic_candle_engulfing(df))
results.append(logic_support_resistance_touch(df))
results.append(logic_volume_breakout(close, volume))
results.append(logic_trend_slope(close))
results.append(logic_breakout_pattern(df))
results.append(logic_atr_volatility(high, low, close))
results.append(logic_doji_signal(df))
results.append(logic_obv_divergence(close, volume))
results.append(logic_fibonacci_zone(price, high.iloc[-1], low.iloc[-1]))
results.append(logic_keltner_channel(close))
results.append(logic_moving_average_stack(close))
results.append(logic_heikin_ashi_trend(df))
results.append(logic_williams_r(close))
results.append(logic_cci_signal(close))
results.append(logic_supertrend_signal(df))
results.append(logic_ttm_squeeze_signal(close))
results.append(logic_golden_cross(close))
results.append(logic_adl_divergence(close, high, low, volume))
results.append(logic_sma_distance_signal(close))
results.append(logic_pivot_point_zone(price, high.iloc[-1], low.iloc[-1], close.iloc[-1]))
results.append(logic_macd_histogram_cross(close))
results.append(logic_ema_ribbon(close))
results.append(logic_hammer_or_shooting_star(df))
results.append(logic_adx_strength(high, low, close))
results.append(logic_inside_bar(df))
results.append(logic_outside_bar(df))
results.append(logic_volume_spike(volume))
results.append(logic_mfi_entry(high, low, close, volume))
results.append(logic_trendline_touch(close))
results.append(logic_bollinger_bands_bounce(close))
results.append(logic_psar_trend(df))

return results

def generate_trade_decision(results): positive = [res for res in results if 'BUY' in res or 'BULLISH' in res or 'SUPPORT' in res or 'BOUNCE' in res] negative = [res for res in results if 'SELL' in res or 'BEARISH' in res or 'RESISTANCE' in res or 'REJECT' in res]

if len(positive) > len(negative) * 1.5:
    return 'BUY', positive
elif len(negative) > len(positive) * 1.5:
    return 'SELL', negative
else:
    return 'NEUTRAL', positive + negative

def signal_engine(df): results = analyze_signals(df) decision, evidence = generate_trade_decision(results) return { 'signal': decision, 'evidence': evidence, 'total_indicators': len(results), 'positives': len([r for r in results if 'BUY' in r or 'BULLISH' in r]), 'negatives': len([r for r in results if 'SELL' in r or 'BEARISH' in r]), }

