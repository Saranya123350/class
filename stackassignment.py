# Stack Implementation
# A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle. The last
# element inserted into the stack is the first one to be removed. It is commonly used for undo
# operations, expression evaluation, and function call management.
# Create: Stack class to implement a Stack Data Structure.
# Classes should have the following methods:
# ● To push an element onto the stack.
# ● To pop an element from the stack (with underflow check - if the stack is already empty
# handle it).
# ● To peek (return the top element without removing it).
# ● To check if the stack is empty or full.
class stack:
    def __init__(self,capacity=None):
        self.val=[]
        self.capacity=capacity
    def push(self,item):
        if self.capacity is not None and len(self.val)>=self.capacity:
            return "stack is full"
        else:
            self.val.append(item)
            return f"{item} added to the stack"
    def pop(self):
        if len(self.val)==0 :
            return "stack is empty, append the elements"
        else:
            first=self.val.pop()
            return f"{first} removed from stack"
    def peek(self):
        if len(self.val) == 0 :
            return "stack is empty"
        else:
            return f"{self.val[-1] } is the top element in the stack"
    def display(self):
        return f"stack elements: {self.val}"
s=stack()
print(s.push(50))
print(s.push(10))
print(s.push(40))
print(s.push(30))
print(s.pop())
print(s.pop())
print(s.push(60))      
print(s.display())

    



