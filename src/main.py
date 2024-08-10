import ccxt
import talib
import numpy as np

def bitcoin_trading_strategy(exchange, symbol, timeframe='1h', ema_fast=10, ema_slow=30, rsi_period=14, rsi_overbought=70, rsi_oversold=30):
    # Fetch historical data
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    closes = np.array([x[4] for x in ohlcv])
    
    # Calculate indicators
    ema_fast = talib.EMA(closes, timeperiod=ema_fast)
    ema_slow = talib.EMA(closes, timeperiod=ema_slow)
    rsi = talib.RSI(closes, timeperiod=rsi_period)
    
    # Generate signals
    last_close = closes[-1]
    last_ema_fast = ema_fast[-1]
    last_ema_slow = ema_slow[-1]
    last_rsi = rsi[-1]
    
    # Trading logic
    if last_ema_fast > last_ema_slow and last_rsi < rsi_oversold:
        return 'BUY'
    elif last_ema_fast < last_ema_slow and last_rsi > rsi_overbought:
        return 'SELL'
    else:
        return 'HOLD'

# Example usage
exchange = ccxt.binance()
symbol = 'BTC/USDT'
signal = bitcoin_trading_strategy(exchange, symbol)
print(f"Current signal: {signal}")