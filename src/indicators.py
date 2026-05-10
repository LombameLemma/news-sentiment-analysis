from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator

def add_indicators(df):

    df['SMA_10'] = SMAIndicator(
        close=df['Adj Close'],
        window=10
    ).sma_indicator()

    df['RSI'] = RSIIndicator(
        close=df['Adj Close'],
        window=14
    ).rsi()

    macd = MACD(close=df['Adj Close'])

    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()

    return df