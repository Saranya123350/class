def uniform(value):
    if len(value)<2:
        return "atleast 2 values must present"
    diff=value[1]-value[0]
    for i in range(1,len(value)-1):
        if value[i+1]-value[i]!=diff :
            return "values are non uniform"
        return "values are uniform"
print(uniform([0, 2, 10, 6, 8]))



