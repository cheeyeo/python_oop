# ONLY AVAILABLE IN PYTHON 3.7 !!!
from dataclasses import make_dataclass

Stock = make_dataclass("Stock", "symbol", "current", "high", "low")
stock = Stock("FB", 177.46, high=178.67, low=175.79)

print(stock)