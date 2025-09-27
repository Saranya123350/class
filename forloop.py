# iteration is for used repeatedly, the data structure which allows to do iteration is called as iteradble data structures.iterator is the which perform iteration by it.
# import time 
# time.sleep(2)       to print character at particular seconds inside we mention.

#  write a python function which takes input of a number and calculates till at some point 
"""
def calsum(a):
    s=0
    for i in range(a+1):
        s+=i
    return s
print(calsum(10))
"""
# input: l1=[1,2,5,7,10],l2=[8,12,9,20,50] output: result= [9, 14, 14, 27, 60]
"""
l1=[1,2,5,7,10]
l2=[8,12,9,20,50] 
sum=0
result=[]
for i in range(len(l1)):
    result.append(l1[i]+l2[i])
print(result)
"""
# input="MISSISSIPPI" O/P: {M:1,I:4,S:4,P:2}
"""
a=list("Saranya")
dict={}
for i in range(len(a)):
    dict[a[i]]=a.count(a[i])
print(dict)
(or)
a=list("Saranya")
dict={}
for i in a:
    dict[i]=a.count(i)
print(dict)
"""

"""
a=["Dog","F","horn","Flight"]
dict={}
for i in a:
    dict[i]=len(i)
print(dict)
"""