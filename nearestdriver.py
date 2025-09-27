# allocate to the nearest driver based on coordinates
import math
def dist(p1,p2):
    val= math.sqrt((p2[0]-p1[0])**2+(p2[0]-p1[0])**2)
    return val
def driver(d1,d2,u):
    if dist(d1,u)<dist(d2,u):
        return "Assign driver 1"
    else:
        return "Assign driver 2"
d1=(2,3)
d2=(7,8)
u=(10,10)    
print(driver(d1,d2,u))
