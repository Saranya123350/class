# Given a list of past monthly sales, calculate the average sales to predict next month’s demand. (Supply Chain)
def predictsales(a):
    net=sum(a)
    return net/len(a)
data=[30,50,70]
print(predictsales(data))