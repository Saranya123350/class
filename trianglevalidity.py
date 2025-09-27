#3 angles of a triangle check its valid or not
def triangle(a,b,c):
    if a+b+c==180:
        return "Valid triangle"
    else:
        return "Invalid triangle"
print(triangle(130,40,60))