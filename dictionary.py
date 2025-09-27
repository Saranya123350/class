# dict is unordered, keys should not be duplicate but values can be duplicate, key is like aa index, 
marks={"physics":["sai",30],"Maths":45}
language={"chemistry":50,"tel":45}
marks["english"]=45
marks.update(language)
"""
print(marks)
print(marks.keys())
print(marks.values())
print(marks.get("hindi"))"""
# user input username and password and store it in dict
# store 3 user names and password in dictionary
# give valid details if not user details are invalid ask use to login and if present in database 
user_details={"ramakrishna@gmail.com":"Saranya@13","sri@gmail.com":"Mana@123","Sai@gmail.com":"Srujana@05"}
if user_details["ramakrishna@gmail.com"]:
    print(["Sai",20,"Cse"])
user_name=input("enter the user_name:")
if user_details.get(user_name)==None : 
    print("Valid user details should be provide for login")
else:
    print("provide the password for login")
    pwd=input("Enter password:")
    if pwd==user_details[user_name]:
        print("Valid password, can login succesfully")
    else:
        print("Invalid password, please provide valid password")



    

