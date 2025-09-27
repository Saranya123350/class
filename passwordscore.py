def password(s):
    special ="!@#$&*<>?"
    score=0
    message=[]
    has_length=False 
    has_spaces=False 
    has_upperlower_chars=False 
    has_special=False 
    has_digits=False
    
    if len(s)>=8:
        has_length=True
    if s.count(" ")==0:
        has_spaces=True
    if (c.isupper() for c in s) and (c.islower() for c in s):
        has_upperlower_chars=True
    if any(i.isdigit() for i in s):
        has_digits=True
    if any(i in special for i in s):
        has_special=True
    if has_length==True: score+=2 
    if has_spaces==True:score+=2 
    if has_upperlower_chars==True  :score+=2 
    if has_digits==True:score+=2 
    if has_special==True:score+=2 
           
    if not has_length:
        return "Password must have atleast 8 characters"
    elif not has_spaces:
        return "Password should not contain spaces"
    elif not has_upperlower_chars:
        return "Password should contain both upper and lower characters" 
    elif not has_digits:
        return "Password should contain atleast 1 digit"
    elif not has_special:
        return "Password should contain atleast 1 special characters "
    if score==10:
        return "Valid password"
   
   
print(password("Kahna@13"))