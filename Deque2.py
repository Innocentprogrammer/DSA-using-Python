# Deque Using Doubly Linked List

# Q1. Define a class Node with instance object member Variables prev, item & next. 

class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev 
        self.data=data 
        self.next=next


# Q2. Define a class Deque to implement deque data structure using doubly linked list concept. Define __init__() method to initialise front and rear reference variable; and item_count variable to keep trrack of number of elements in the deque.

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None 
        self.item_count=0


# Q3. Define a method is_empty() to check if the Deque class. 

    def is_empty(self):
        return self.front==None


# Q4. In Deque class, define insert_front() method to add data at front end of the deque.

    def insert_front(self,data):
        newNode=Node(None,data,self.front)
        if not self.is_empty():
            self.front.prev=newNode
        else:
            self.rear=newNode
        self.front=newNode
        self.item_count+=1


# Q5. In Deque class, define insert_rear() method to add data at rear end of the deque.

    def insert_rear(self,data):
        newNode=Node(self.rear,data)
        if not self.is_empty():
            self.rear.next=newNode
        else:
            self.front=newNode
        self.rear=newNode 
        self.item_count+=1  


# Q6. In Deque class, define delete_front() method to remove front element from the deque.

    def delete_front(self):
        temp=self.front.data
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.front=self.front.next 
            self.front.prev= None
        self.item_count-=1
        return temp


# Q7. In Deque class, define delete_rear() method to remove rear element from the deque.

    def delete_rear(self):
        temp=self.rear.data
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            self.rear=self.rear.prev 
            self.rear.next= None
        self.item_count-=1
        return temp



# Q8. In Deque class, define get_front() method to return front element of the deque.

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.front.data


# Q9. In Deque class, define get_rear() method to return rear element of the deque.

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.rear.data


# Q10. In Deque class, define size() method to return size of the deque that is number of items present in deque.

    def size(self):
        if self.is_empty():
            return 0
        else:
            return self.item_count
        

#Driver Code
mydeque=Deque()
mydeque.insert_rear(3)
mydeque.insert_rear(4)
mydeque.insert_front(2)
mydeque.insert_front(1)
mydeque.insert_rear(5)
print("front: ",mydeque.get_front(),", rear: ",mydeque.get_rear(),", size: ",mydeque.size())
print("Deque element from front: ",mydeque.delete_front())
print("Deque element from rear: ",mydeque.delete_rear())
print("front: ",mydeque.get_front(),", rear: ",mydeque.get_rear(),", size: ",mydeque.size())
