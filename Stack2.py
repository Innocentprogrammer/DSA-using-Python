# Stack Extending List

# Q1. Define a class Stack to implement stack data structure by extending list class. 

class Stack(list):
    

# Q2. Define a method is_empty() to check if stack is empty in Stack class.

    def is_empty(self):
        return len(self)==0 


# Q3. In Stack class, define push() method to add data onto the stack. 

    def push(self,data):
        return self.append(data)

        

# Q4. In Stack class, define pop() method to remove top element from the stack. 

    def popped(self):
        if not self.is_empty():
            return self.pop() 
        else:
            raise OverflowError("Stack is Empty")


# Q5. In Stack class, define peak() method to return top element on the stack.

    def peak(self):
        if not self.is_empty():
            return self[-1] 
        else:
            raise IndexError("Stack is Empty")


# Q6. In Stack class, define size() method to return size of the stack that is number of items present in the stack. 

    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            raise IndexError("Stack is Empty")
        


# Q7. Implement a way to restrict use of insert() method of list class from stack object.

    def insert(self,index,data):
        raise AttributeError("Stack does not support insert() method")
    
mylist = Stack()

mylist.push(1)
mylist.push(2)
mylist.push(3)
mylist.push(4)
print("Peak Element: ",mylist.peak())
print("Size of Stack: ",mylist.size())
print("Pop Element: ",mylist.popped())
print("Pop Element: ",mylist.popped())
print("Peak Element: ",mylist.peak())
print("Size of Stack: ",mylist.size())
