# Stack Using List 

# Q1. Define a class Stack to implement stack data structure using list. Define __init__() method to create an empty list object as instance object member of Stack. 

class Stack:
    def __init__(self):
        self.list=[]


# Q2. Define a method is_empty() to check if the stack is empty in Stack class.

    def is_empty(self):
        return len(self.list)==0


# Q3. In Stack class, define push() method to add data onto the stack.

    def push(self,data):
        self.list.append(data)
        print(self.list)


# Q4. In Stack class, define pop() method to remove top element from the stack.

    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        else: 
            raise OverflowError("Stack is Empty")


# Q5. In Stack class, define peak() method to return top element on the stack.

    def peak(self):
        if not self.is_empty():
            for i in range(self.size()):
                if i+1==self.size():
                    return self.list[i] 
        else: 
            raise ValueError("There is no any element in stack")



# Q6. In Stack class, define size() method to return the size of the stack that is number of element items present in the stack.

    def size(self):
        return len(self.list) 
    

#Driver Code 
mylist = Stack()
mylist.push(1)
mylist.push(2)
mylist.push(3)
mylist.push(4)
mylist.push(5)
mylist.push(6)
print("Peak of list: ",mylist.peak())
print("list size: ",mylist.size())
print("Popped Element: ",mylist.pop())
print("Peak of list: ",mylist.peak())
print("list size: ",mylist.size())

