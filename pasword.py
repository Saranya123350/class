def password(s):
    special ="!@#$&*<>?"
    if len(s)<8:
        return "Password must have atleast 8 characters"
    elif s.count(" ")>=1 :
        return "Password should not contain spaces"
    elif s.isupper()==True or s.islower()==True :
        return "Password should contain both upper and lower characters"
    elif not any(i.isdigit() for i in s):
        return "atleast 1 digit should be present in password"
    elif not any(i in special for i in s):
        return "Password should contain atleast 1 special characters "
    return "Valid password"
print(password("Kahna$122"))
 


