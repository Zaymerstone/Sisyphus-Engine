import datetime as dt
import yfinance as yf
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import talib

def interface_backtest(uc_strategy, uc_ticker, uc_start_year, uc_start_month, uc_end_year, uc_end_month, **kwargs):

    # Check if uc_strategy is not SmaCross or SmaCross2

    if uc_strategy not in ["SmaCross", "SmaCross2"]:
        raise ValueError("Invalid uc_strategy: {}. Allowed values: 'SmaCross', 'SmaCross2'.".format(uc_strategy))

    # Check if uc_ticker is not in GOOG, MSFT, TSLA

    allowed_tickers = ["GOOG", "MSFT", "TSLA"]
    if uc_ticker not in allowed_tickers:
        raise ValueError("Invalid uc_ticker: {}. Allowed tickers: {}.".format(uc_ticker, ', '.join(allowed_tickers)))

    class SmaCross(Strategy):
        def init(self, sma1_period=10, sma2_period=20):
            price = self.data.Close
            self.ma1 = self.I(SMA, price, sma1_period)
            self.ma2 = self.I(SMA, price, sma2_period)

        def next(self):
            if crossover(self.ma1, self.ma2):
                self.buy()
            elif crossover(self.ma2, self.ma1):
                self.sell()

    class RSI0scillator(Strategy):

        class RSI0scillator(Strategy):
            def init(self, upper_bound=70, lower_bound=30, rsi_window=14):
                self.upper_bound = upper_bound
                self.lower_bound = lower_bound
                self.rsi_window = rsi_window
                self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)

        def next(self):
            if crossover(self.rsi, self.upper_bound):
                self.position.close()
            elif crossover(self.lower_bound, self.rsi):
                self.buy()

    start = dt.datetime(uc_start_year, uc_start_month, 1)
    end = dt.datetime(uc_end_year, uc_end_month, 1)
    data = yf.download(uc_ticker, start=start, end=end)

    if uc_strategy == "SmaCross":
        selected_strategy = SmaCross
    elif uc_strategy == "RSI0scillator":
        selected_strategy = RSI0scillator

    bt = Backtest(data, selected_strategy, commission=.002, exclusive_orders=True, **kwargs)
    bt.run()
    bt.plot()







