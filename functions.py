# module called areas, funtion to calculate volume of a sphere(4/3*3.14*r**2), volume of a cuboid(l*b*h)
import math
def volumeofsphere(radius):
    res=(4/3)*math.pi*(radius)**2
    return res 
def volumeofcuboid(length,breadth,height):
    result=length*breadth*height
    return result 
print(volumeofsphere(4))
print(volumeofcuboid(4,5,6))