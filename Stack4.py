# Stack Using Singly Linked List file

# Q1. Import module containing singly linked list code in your python file.

from SinglyLinkedList import *


# Q2. Define a class Stack to implement stack data structure. Define __init__() method to create Singly Linked List(SLL) object

class Stack():
    def __init__(self):
        self.top=SLL()
        self.item_count=0


# Q3. Define a method is_empty() to check if the stack is empty in Stack class. 

    def is_empty(self):
        return self.top.is_empty()


# Q4. In Stack class, define push() method to add data onto the stack.

    def push(self,data):
        if not self.top.insert_at_last(data):
            self.top.insert_at_start(data)
            self.item_count+=1


# Q5. In Stack class, define pop() method to remove top element from the stack.

    def pop(self):
        if not self.top.is_empty():
            print("Popped Element",self.top.head.item)
            self.top.delete_first()
            self.item_count-=1


# Q6. In Stack class, define peak() method to return top element on the stack.

    def peak(self):
        if not self.top.is_empty():
            return self.top.head.item
        

# Q7. In Stack class, define size() method to return size of the stack that is number of items present in the stack.
    
    def size(self):
        return self.item_count
    

#Driver Code 
mystack=Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(5)
print("Peak Element: ",mystack.peak())
print("Total No. of Element: ",mystack.size())
mystack.pop()
print("Peak Element: ",mystack.peak())
print("Total No. of Element: ",mystack.size())