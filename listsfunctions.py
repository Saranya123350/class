#  2 lists(even,odd) user input
s=int(input("enter number:"))
even_list =[]
odd_list=[]
if s%2==0:
    even_list.append(s)
else:
    odd_list.append(s)
print(even_list)
print(odd_list)

#check if an element exist 
s=input("enter input: ")
list_1 =["sai","saranya","krishna"]
if list_1.count("s")>=1:
    print("Present")
else:
    print("Not present")