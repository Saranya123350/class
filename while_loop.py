# # to store the odd numbers from 0 to 100 in list
# a=0
# s=[]
# while a<100: 
#     if a%2!=0:
#         s.append(a)
#     a=a+1
# print(s)

# #  even squares in dict
# a=2 
# dict ={}
# while a<101:
#     if a%2==0:
#         dict[a]=a**2
#     a+=1 
# print(dict)

# build a function to print table
# def table(a):
#     b=1
#     while b<=10:
#         tab=print(a,"x",b,"=",a*b)
#         b+=1 
#     return tab
# print(table(4))

letters=['A','B','C','D','E','F','G','H']
l1=[]
l2=[]
# O/P:- L1=[A,C,E,G], L2=[B,D,F,H]
a=0
while a<len(letters):
    if a %2==0:
        l1.append(letters[a])
    else:
        l2.append(letters[a])
    a+=1
print(l1)
print(l2)