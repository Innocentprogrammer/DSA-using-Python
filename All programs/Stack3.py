# Stack Using Linked List

# Q1. Define a class Stack to implement stack data structure using Singly Linked List concept. Define __init__() method to initialise start reference variable and item_count variable to keep track of number of elements in stack.

class Node:
    def __init__(self,data=None,next=None):
        self.data=data 
        self.next=next 
    
class Stack:
    def __init__(self,top=None,data_count=0):
        self.top=top
        self.data_count=data_count


# Q2. Define a method is_empty() to check if stack is empty in Stack class.

    def is_empty(self):
        return self.top==None 


# Q3. In Stack class, define push() method to add data onto the stack.

    def push(self,data):
        newNode=Node(data,self.top)
        self.top=newNode
        self.data_count+=1



# Q4. In Stack class, define pop() method to remove top element from the stack.

    def pop(self):
        if not self.is_empty():
            print("Popped Element: ",self.top.data)
            self.top=self.top.next 
            self.data_count-=1
        else:
            raise IndexError("Stack is empty")


# Q5. In Stack class, define peak() method to return top element on the stack.

    def peak(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("Stack is empty")


# Q6. In Stack class, define size() method to return size of the stack that is number of items present in the stack.

    def size(self):
        return self.data_count

#Driver code
mystack=Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
print("Peak Element: ",mystack.peak())
print("Size of Stack: ",mystack.size())
mystack.pop()
mystack.pop()
print("Peak Element: ",mystack.peak())
print("Size of Stack: ",mystack.size())
