cities=['chennai','hyderabad',"valaparla","banglore"]
numbers=[1,2,3,4]
# This style of bulding structures which can be accomidate multiple types of values is called oject.
# These structures are called objections even strings and int 

# -------------------------OOPS---------------------------------------------------------------------
# CLASS is a keyword that uses before specifying name of the class
# class Rectangle:
#     shape="2D rectangle"
#     def __init__(self,length,breadth):
#         self.length=length 
#         self.breadth=breadth 
#     def getLength(self):
#         return self.length 
#     def getBreadth(self):
#         return self.breadth
#     def area(self):
#         return self.length * self.breadth
# my_rectangle=Rectangle(10,10)
# other_rectangle=Rectangle(5,5)
# a=other_rectangle.area()
# print(a)
# # Object oriented programming in python:
# object oriented programming is a programming construct where we build elements as objects
# objects combine data and method 

# create a point(x,y) using classes and method to show x and y values
# class point:
#     def __init__(self,x_coord,y_coord):
#         self.x_coord=x_coord 
#         self.y_coord=y_coord 
#     def get_x(self):
#         return self.x_coord 
#     def get_y(self):
#         return self.y_coord 
# my_point=point(4,5)
# oth_point=point(6,7)
# print(my_point.get_x())

class point:
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
    def distance(self,oth_point):
        return ((oth_point.x - self.x)**2+(oth_point.y - self.y)**2)**0.5
p1=point(1,2)
p2=point(3,4)

print(p1.distance(p2))
