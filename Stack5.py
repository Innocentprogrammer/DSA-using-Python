# Stack By Extending Singly Linked List File 

# Q1. Import module containing singly linked list code in your python file.

from SinglyLinkedList import *


# Q2. Define a class Stack to implement stack data structure by inheriting linked list class.

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    
    
# Q3. Define a method is_empty() to check if the stack is empty in Stack class.

    def is_empty(self):
        return super().is_empty()


# Q4. In Stack class, define push() method to add data onto the stack.

    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1


# Q5. In Stack class, define pop() method to remove top element from the stack.

    def pop(self):
        if not self.is_empty():
            print("Popped Element: ",self.head.item)
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack is empty")


# Q6. In Stack class, define peak() method to return top element on the stack.

    def peak(self):
        if not self.is_empty():
            return self.head.item
        else:
            raise IndexError("Stack is empty")


# Q7. In Stack class, define size() method to return size of the stack that is number of item present in stack.

    def size(self):
        return self.item_count
    
#Driver Code:
mystack=Stack()
mystack.push(1)
mystack.push(2)
mystack.push(4)
mystack.push(5)
print("Top element of stack: ",mystack.peak())
print("Total No. of element",mystack.size())
mystack.pop()
print("Top element of stack: ",mystack.peak())
print("Total No. of element",mystack.size())

