# calculate euclidean and manheten distances
import math
def euclidian(a,b,c,d):
    res=math.sqrt((a-c)**2+(b-d)**2)
    return res 
def manhattan(x1,x2,x3,x4):
    result=abs((x3-x1)**2+(x4-x2)**2)
    return result 
print(manhattan(4,5,6,7))
print(euclidian(2,3,4,5))

    