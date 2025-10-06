#. Given a list of daily stock prices, write a program to calculate the average stock price. 
def stock(a):
    return sum(a)/len(a)
stockprice=[1000,3000,6000,2000,3000]
print(stock(stockprice))