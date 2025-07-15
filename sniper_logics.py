def logic_ema_stack(prices, ema_periods=[5, 7, 14, 21]):
    """
    Add-on 1: EMA Stack Confirmation
    Check if EMAs are stacked correctly for trend confirmation.
    """
    from ta.trend import EMAIndicator
    emas = [EMAIndicator(prices, window=p).ema_indicator() for p in ema_periods]
    is_bullish = all(emas[i].iloc[-1] > emas[i+1].iloc[-1] for i in range(len(emas)-1))
    is_bearish = all(emas[i].iloc[-1] < emas[i+1].iloc[-1] for i in range(len(emas)-1))
    return 'BUY' if is_bullish else 'SELL' if is_bearish else 'WAIT'

def logic_price_above_ema(prices, ema_period=21):
    """
    Add-on 2: Price Above or Below EMA
    """
    from ta.trend import EMAIndicator
    ema = EMAIndicator(prices, window=ema_period).ema_indicator()
    return 'BUY' if prices.iloc[-1] > ema.iloc[-1] else 'SELL'

def logic_rsi_overbought_oversold(prices, rsi_period=14):
    """
    Add-on 3: RSI Overbought/Oversold
    """
    from ta.momentum import RSIIndicator
    rsi = RSIIndicator(prices, window=rsi_period).rsi()
    if rsi.iloc[-1] < 30:
        return 'BUY'
    elif rsi.iloc[-1] > 70:
        return 'SELL'
    else:
        return 'WAIT'

def logic_macd_cross(prices):
    """
    Add-on 4: MACD Cross
    """
    from ta.trend import MACD
    macd = MACD(prices)
    if macd.macd_diff().iloc[-1] > 0 and macd.macd_diff().iloc[-2] < 0:
        return 'BUY'
    elif macd.macd_diff().iloc[-1] < 0 and macd.macd_diff().iloc[-2] > 0:
        return 'SELL'
    else:
        return 'WAIT'

def logic_bollinger_band_bounce(prices):
    """
    Add-on 5: Bollinger Band Bounce
    """
    from ta.volatility import BollingerBands
    bb = BollingerBands(prices)
    if prices.iloc[-1] < bb.bollinger_lband().iloc[-1]:
        return 'BUY'
    elif prices.iloc[-1] > bb.bollinger_hband().iloc[-1]:
        return 'SELL'
    else:
        return 'WAIT'

def logic_candle_reversal(prices):
    """
    Add-on 6: Reversal Candle Pattern (Simple)
    """
    if prices.iloc[-1] > prices.iloc[-2] and prices.iloc[-2] < prices.iloc[-3]:
        return 'BUY'
    elif prices.iloc[-1] < prices.iloc[-2] and prices.iloc[-2] > prices.iloc[-3]:
        return 'SELL'
    else:
        return 'WAIT'

def logic_volume_spike(volume):
    """
    Add-on 7: Volume Spike Detection
    """
    avg_volume = volume.rolling(window=10).mean()
    if volume.iloc[-1] > 1.5 * avg_volume.iloc[-1]:
        return 'VOLUME SPIKE'
    return 'NORMAL'
def logic_fibonacci_retrace(prices):
    """
    Add-on 13: Fibonacci Retracement Zones (Simple)
    """
    high = prices.max()
    low = prices.min()
    current = prices.iloc[-1]
    levels = [0.236, 0.382, 0.5, 0.618, 0.786]
    retracements = [(high - (high - low) * level) for level in levels]

    for level in retracements:
        if abs(current - level) / current < 0.01:
            return f'NEAR FIB LEVEL {level:.2f}'
    return 'NO FIB LEVEL NEAR'

def logic_heikin_ashi_trend(df):
    """
    Add-on 14: Heikin Ashi Trend Detection
    """
    ha_close = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    trend = 'UP' if ha_close.iloc[-1] > ha_close.iloc[-2] else 'DOWN'
    return f'HA TREND: {trend}'

def logic_obv(prices, volume):
    """
    Add-on 15: On-Balance Volume Momentum
    """
    obv = [0]
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            obv.append(obv[-1] + volume[i])
        elif prices[i] < prices[i - 1]:
            obv.append(obv[-1] - volume[i])
        else:
            obv.append(obv[-1])
    return 'OBV UP' if obv[-1] > obv[-2] else 'OBV DOWN'

def logic_stochastic(prices, high, low):
    """
    Add-on 16: Stochastic Oscillator Entry
    """
    from ta.momentum import StochasticOscillator
    stoch = StochasticOscillator(high=high, low=low, close=prices)
    if stoch.stoch_signal().iloc[-1] < 20:
        return 'BUY'
    elif stoch.stoch_signal().iloc[-1] > 80:
        return 'SELL'
    return 'WAIT'

def logic_engulfing_candle(df):
    """
    Add-on 17: Bullish or Bearish Engulfing Candle Pattern
    """
    open1, close1 = df['open'].iloc[-2], df['close'].iloc[-2]
    open2, close2 = df['open'].iloc[-1], df['close'].iloc[-1]
    if close1 < open1 and close2 > open2 and close2 > open1 and open2 < close1:
        return 'BULLISH ENGULFING'
    elif close1 > open1 and close2 < open2 and close2 < open1 and open2 > close1:
        return 'BEARISH ENGULFING'
    return 'NONE'

def logic_breakout_range(prices):
    """
    Add-on 18: Range Breakout Detection
    """
    recent = prices[-20:]
    high = recent.max()
    low = recent.min()
    if prices.iloc[-1] > high:
        return 'BREAKOUT UP'
    elif prices.iloc[-1] < low:
        return 'BREAKOUT DOWN'
    return 'INSIDE RANGE'

def logic_marubozu(df):
    """
    Add-on 19: Marubozu Candle
    """
    last_open = df['open'].iloc[-1]
    last_close = df['close'].iloc[-1]
    last_high = df['high'].iloc[-1]
    last_low = df['low'].iloc[-1]
    if last_close == last_high and last_open == last_low:
        return 'BULLISH MARUBOZU'
    elif last_close == last_low and last_open == last_high:
        return 'BEARISH MARUBOZU'
    return 'NONE'

def logic_doji(df):
    """
    Add-on 20: Doji Candle
    """
    last_open = df['open'].iloc[-1]
    last_close = df['close'].iloc[-1]
    if abs(last_close - last_open) <= (0.001 * last_open):
        return 'DOJI'
    return 'NORMAL'

def logic_wick_rejection(df):
    """
    Add-on 21: Wick Rejection Candle
    """
    candle = df.iloc[-1]
    body = abs(candle['open'] - candle['close'])
    wick = candle['high'] - candle['low']
    if wick > 2 * body:
        return 'WICK REJECTION'
    return 'NORMAL'

def logic_three_candle_pattern(df):
    """
    Add-on 22: Three Candle Reversal
    """
    if df['close'].iloc[-1] > df['close'].iloc[-2] > df['close'].iloc[-3]:
        return 'THREE BULL CANDLES'
    elif df['close'].iloc[-1] < df['close'].iloc[-2] < df['close'].iloc[-3]:
        return 'THREE BEAR CANDLES'
    return 'NONE'

def logic_moving_average_slope(prices, period=21):
    """
    Add-on 23: MA Slope Direction
    """
    from ta.trend import SMAIndicator
    ma = SMAIndicator(prices, window=period).sma_indicator()
    slope = ma.iloc[-1] - ma.iloc[-2]
    if slope > 0:
        return 'MA UP'
    elif slope < 0:
        return 'MA DOWN'
    return 'FLAT'

def logic_rsi_divergence(prices, rsi_period=14):
    """
    Add-on 24: RSI Divergence (Basic)
    """
    from ta.momentum import RSIIndicator
    rsi = RSIIndicator(prices, window=rsi_period).rsi()
    if prices.iloc[-1] > prices.iloc[-2] and rsi.iloc[-1] < rsi.iloc[-2]:
        return 'BEARISH DIVERGENCE'
    elif prices.iloc[-1] < prices.iloc[-2] and rsi.iloc[-1] > rsi.iloc[-2]:
        return 'BULLISH DIVERGENCE'
    return 'NO DIVERGENCE'
def logic_adx_trend(prices, high, low):
    """
    Add-on 8: ADX Strength Filter
    """
    from ta.trend import ADXIndicator
    adx = ADXIndicator(high=high, low=low, close=prices)
    if adx.adx().iloc[-1] > 25:
        return 'TRENDING'
    else:
        return 'RANGING'

def logic_support_resistance_zone(prices):
    """
    Add-on 9: Support/Resistance Reaction
    """
    recent = prices[-20:]
    support = min(recent)
    resistance = max(recent)
    current = prices.iloc[-1]
    if abs(current - support) < (resistance - support) * 0.1:
        return 'NEAR SUPPORT'
    elif abs(current - resistance) < (resistance - support) * 0.1:
        return 'NEAR RESISTANCE'
    return 'MIDDLE'

def logic_trend_strength(prices):
    """
    Add-on 10: Trend Momentum via Linear Regression
    """
    from sklearn.linear_model import LinearRegression
    import numpy as np
    x = np.arange(len(prices)).reshape(-1, 1)
    y = prices.values.reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    slope = model.coef_[0][0]
    if slope > 0:
        return 'UP TREND'
    elif slope < 0:
        return 'DOWN TREND'
    return 'FLAT'

def logic_supertrend_entry(prices, high, low):
    """
    Add-on 11: SuperTrend Confirmation
    """
    from ta.trend import MACD  # Placeholder; replace with custom supertrend logic if needed
    macd = MACD(prices)
    return 'BUY' if macd.macd_diff().iloc[-1] > 0 else 'SELL'

def logic_ema_crossover(prices, short_period=9, long_period=21):
    """
    Add-on 12: EMA Crossover
    """
    from ta.trend import EMAIndicator
    short_ema = EMAIndicator(prices, window=short_period).ema_indicator()
    long_ema = EMAIndicator(prices, window=long_period).ema_indicator()
    if short_ema.iloc[-2] < long_ema.iloc[-2] and short_ema.iloc[-1] > long_ema.iloc[-1]:
        return 'BUY'
    elif short_ema.iloc[-2] > long_ema.iloc[-2] and short_ema.iloc[-1] < long_ema.iloc[-1]:
        return 'SELL'
    return 'WAIT'
  def logic_pivot_point_zone(price, high, low, close):
    """
    Add-on 25: Pivot Point Zone Confluence
    """
    pivot = (high + low + close) / 3
    r1 = 2 * pivot - low
    s1 = 2 * pivot - high
    if abs(price - pivot) / price < 0.01:
        return 'NEAR PIVOT'
    elif abs(price - r1) / price < 0.01:
        return 'NEAR RESISTANCE 1'
    elif abs(price - s1) / price < 0.01:
        return 'NEAR SUPPORT 1'
    return 'AWAY FROM PIVOT'

def logic_macd_histogram_cross(prices):
    """
    Add-on 26: MACD Histogram Cross Zero
    """
    from ta.trend import MACD
    macd = MACD(prices)
    hist = macd.macd_diff()
    if hist.iloc[-2] < 0 and hist.iloc[-1] > 0:
        return 'BULLISH MACD CROSS'
    elif hist.iloc[-2] > 0 and hist.iloc[-1] < 0:
        return 'BEARISH MACD CROSS'
    return 'NO CROSS'

def logic_ema_ribbon(prices):
    """
    Add-on 27: EMA Ribbon Compression
    """
    from ta.trend import EMAIndicator
    ema_9 = EMAIndicator(prices, window=9).ema_indicator()
    ema_21 = EMAIndicator(prices, window=21).ema_indicator()
    ema_50 = EMAIndicator(prices, window=50).ema_indicator()
    if abs(ema_9.iloc[-1] - ema_21.iloc[-1]) < 0.0005 and abs(ema_21.iloc[-1] - ema_50.iloc[-1]) < 0.0005:
        return 'EMA RIBBON COMPRESSION'
    return 'NORMAL'

def logic_hammer_or_shooting_star(df):
    """
    Add-on 28: Hammer / Shooting Star Pattern
    """
    c = df.iloc[-1]
    body = abs(c['open'] - c['close'])
    upper_wick = c['high'] - max(c['open'], c['close'])
    lower_wick = min(c['open'], c['close']) - c['low']
    if lower_wick > 2 * body:
        return 'HAMMER'
    elif upper_wick > 2 * body:
        return 'SHOOTING STAR'
    return 'NONE'

def logic_adx_strength(high, low, close):
    """
    Add-on 29: ADX Trend Strength
    """
    from ta.trend import ADXIndicator
    adx = ADXIndicator(high=high, low=low, close=close).adx()
    if adx.iloc[-1] > 25:
        return 'STRONG TREND'
    return 'WEAK TREND'

def logic_inside_bar(df):
    """
    Add-on 30: Inside Bar Pattern
    """
    prev = df.iloc[-2]
    curr = df.iloc[-1]
    if curr['high'] < prev['high'] and curr['low'] > prev['low']:
        return 'INSIDE BAR'
    return 'NONE'

def logic_outside_bar(df):
    """
    Add-on 31: Outside Bar Pattern
    """
    prev = df.iloc[-2]
    curr = df.iloc[-1]
    if curr['high'] > prev['high'] and curr['low'] < prev['low']:
        return 'OUTSIDE BAR'
    return 'NONE'

def logic_volume_spike(volume):
    """
    Add-on 32: Volume Spike Detection
    """
    avg_vol = volume[-10:].mean()
    if volume.iloc[-1] > 2 * avg_vol:
        return 'VOLUME SPIKE'
    return 'NORMAL'

def logic_mfi_entry(high, low, close, volume):
    """
    Add-on 33: Money Flow Index Buy/Sell Signal
    """
    from ta.volume import MFIIndicator
    mfi = MFIIndicator(high=high, low=low, close=close, volume=volume).money_flow_index()
    if mfi.iloc[-1] < 20:
        return 'MFI BUY'
    elif mfi.iloc[-1] > 80:
        return 'MFI SELL'
    return 'MFI NEUTRAL'

def logic_trendline_touch(prices):
    """
    Add-on 34: Simulated Trendline Touch (approximation using rolling high/low)
    """
    high = prices.rolling(window=20).max()
    low = prices.rolling(window=20).min()
    if abs(prices.iloc[-1] - high.iloc[-1]) / prices.iloc[-1] < 0.01:
        return 'NEAR UPPER TRENDLINE'
    elif abs(prices.iloc[-1] - low.iloc[-1]) / prices.iloc[-1] < 0.01:
        return 'NEAR LOWER TRENDLINE'
    return 'NO TRENDLINE TOUCH'

def logic_bollinger_bands_bounce(prices):
    """
    Add-on 35: Bollinger Bands Bounce Entry
    """
    from ta.volatility import BollingerBands
    bb = BollingerBands(close=prices)
    lower = bb.bollinger_l()
    upper = bb.bollinger_h()
    if abs(prices.iloc[-1] - lower.iloc[-1]) / prices.iloc[-1] < 0.01:
        return 'BOUNCE LOWER BAND'
    elif abs(prices.iloc[-1] - upper.iloc[-1]) / prices.iloc[-1] < 0.01:
        return 'REJECT UPPER BAND'
    return 'INSIDE BANDS'

def logic_psar_trend(df):
    """
    Add-on 36: Parabolic SAR Trend Filter
    """
    from ta.trend import PSARIndicator
    psar = PSARIndicator(high=df['high'], low=df['low'], close=df['close'])
    if df['close'].iloc[-1] > psar.psar().iloc[-1]:
        return 'PSAR BUY'
    elif df['close'].iloc[-1] < psar.psar().iloc[-1]:
        return 'PSAR SELL'
    return 'PSAR NEUTRAL'
