 

class StockMarket:
    def __init__(self):
        self.stocks = []
        self.traders = []

    def addStock(self, stock_list):
        self.stocks.extend(stock_list)
        print("Stocks added to the market")

    def addTrader(self, trader_list):
        self.traders.extend(trader_list)
        print("Traders added to the market")

    def updateStockPrice(self, stock_name, new_price):
        for stock in self.stocks:
            if stock.name == stock_name:
                stock.updatePrice(new_price)
                return
        print(f"Stock {stock_name} not found in market")

   
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.history = []

    def updatePrice(self, new_price):
        self.price = new_price
        self.history.append(new_price)
        print(f"Stock {self.name} price updated to {self.price}")


class Trader:
    def __init__(self, name):
        self.name = name
        self.portfolio = {} 
        self.transactions = []   

    def buyStock(self, stock, quantity):
        
        if stock.name in self.portfolio:
            self.portfolio[stock.name] += quantity
        else:
            self.portfolio[stock.name] = quantity
            self.transactions.append(f"Bought {quantity} of {stock.name}")
            print(f"{self.name} bought {quantity} shares of {stock.name}")

    def sellStock(self, stock, quantity):
        if stock.name not in self.portfolio or self.portfolio[stock.name] < quantity:
            print(f" No enough shares to sell for {stock.name}")
        else:
            self.portfolio[stock.name] -= quantity
            self.transactions.append(f"Sold {quantity} of {stock.name}")
            print(f"{self.name} sold {quantity} shares of {stock.name}")

    def viewPortfolio(self):
        print(f"{self.name}'s Portfolio:")
        for stock, qty in self.portfolio.items():
            print(f"{stock}: {qty}")

    def viewTransactions(self):
        print(f"{self.name}'s Transactions:")
        for trans in self.transactions:
            print(trans)

S1 = Stock("Apple", 150)
S2 = Stock("fresh juice", 2800)
T1 = Trader("Alice")
T2 = Trader("Bob")

M = StockMarket()

M.addStock([S1, S2])
M.addTrader([T1, T2])


T1.buyStock(S1, 5)
T1.buyStock(S2, 1)
T2.buyStock(S1, 3)
T1.sellStock(S1, 2)
T1.viewPortfolio()
T1.viewTransactions()
M.updateStockPrice("Apple", 120)

