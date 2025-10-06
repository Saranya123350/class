""" A Queue is a linear data structure that follows the FIFO (First In, First Out) principle. The first
element inserted is the first one to be removed. It is widely used in scheduling, resource
allocation, and printer job management.
Create: Queue class to implement a Queue Data Structure.
Classes should have the following methods:
● To enqueue (insert) an element into the queue.
● To dequeue (remove) an element from the queue (with underflow check).
● To peek (view the front element).
● To check if the queue is empty or full  """


class Queue:
    def __init__(self,capacity=None):
        self.val=[]
        self.capacity=capacity
    def enqueue(self,item):
        if self.capacity is not None and len(self.val)>=self.capacity:
            return "Queue is full"
        else:
            self.val.append(item)
            return f"{item} added to the Queue"
    def dequeue(self):
        if len(self.val)==0 :
            return "queue is empty, append the elements"
        else:
            first=self.val.pop(0)
            return f"{first} removed from Queue"
    def peek(self):
        if len(self.val) == 0 :
            return "queue is empty"
        else:
            return f"{self.val[0] } is the front element in the queue"
    def display(self):
        return f"Queue elements: {self.val}"
s=Queue()
print(s.enqueue(50))
print(s.enqueue(10))
print(s.enqueue(40))
print(s.enqueue(30))
print(s.dequeue())
print(s.dequeue())
print(s.enqueue(60))      
print(s.display())

    



