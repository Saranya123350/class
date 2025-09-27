# def cube(s):
#     if s<0:
#         raise ValueError("input canot be negative")
#     else:
#         return(s**2)
# print(cube(0))

# function to withdraw and return balnce  if withdraw amt is negative raise an error 
def withdraw(amt,total):
    if amt<=0:
        raise ValueError("withdrawal amount should be postive")
    else:
        print("balance amount:",total-amt )
    try:
        amt<=0 
    except:
        print("withdrawal amount should be postive")
print(withdraw(-5000,8000))
