# Write a short Python function, minmax(data), that takes a list of three or more numbers,and returns the smallest and largest number
def minmax(a):
    if len(a)<3:
        return "length must be greater than or equal to 3"
    return min(a),max(a)
data=[455,34,67,879]
print(minmax(data))