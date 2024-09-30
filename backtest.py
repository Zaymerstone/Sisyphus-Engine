import datetime as dt
import yfinance as yf
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


start = dt.datetime(2020, 1, 1)
end = dt.datetime(2022, 1, 1)
data = yf.download("MSFT", start=start, end=end)

bt = Backtest(data, SmaCross, commission=.002,
              exclusive_orders=True)

print(bt.run())
bt.plot()