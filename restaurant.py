# restaurent service should in radius
import math 
def restaurantrange(user_loc,res_loc,radius):
    if math.dist(user_loc,res_loc)<=radius :
        return "Accept the order"
    else:
        return "Reject the order"
    
u=(1,2)
r=(6,7)
print(restaurantrange(u,r,9))