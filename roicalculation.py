def rateofinterest(f,i):
    net_profit=f-i
    roi=(net_profit/i)*100
    return roi 
initial_price=200
final_price=600
print(rateofinterest(final_price,initial_price))
