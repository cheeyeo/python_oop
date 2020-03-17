from collections import namedtuple

Stock = namedtuple("Stock", ["symbol", "current", "high", "low"])

stock = Stock("FB", 177.46, high=178.67, low=175.79)
print(stock.symbol)
print(stock.high)

symbol, current, high, low = stock
print(current)

stock.current = 14 # raise error as tuples are immutable!