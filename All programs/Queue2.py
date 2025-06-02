# Queue Using Singly Linked List

# Q1. Define a class Queue to implement queue data structure using singly linked list concept. Define __init__() method to initialise front and rear reference variable; and item_count variable to keep track of number of elements in the queue. 

class Node:
    def __init__(self,data=None, next=None):
        self.data=data 
        self.next=next 
    
class Queue: 
    def __init__(self,front=None): 
        self.front=front
        self.rear=None
        self.item_count=0


# Q2. Define a method is_empty() to check if the queue is empty in Queue class.

    def is_empty(self):
        return self.front==None


# Q3. In Queue class, define enqueue() method to add data into the queue. 

    def enqueue(self,data):
        newNode=Node(data)
        if not self.is_empty():
            self.rear.next=newNode
        else:
            self.front=newNode
        self.rear=newNode
        self.item_count+=1


# Q4. In Queue class, define dequeue() method to remove front element from the queue. 

    def dequeue(self):
        print("Dequeue Element= ",self.front.data)
        if not self.is_empty(): 
            self.front=self.front.next 
        elif self.front==self.rear:
            self.front=self.rear=None
        else: raise IndexError("Queue is empty")
        self.item_count-=1



# Q5. In Queue class, define get_front() method to return front element of the queue. 

    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else: raise IndexError("Queue is empty")


# Q6. In Queue class, define get_rear() method to return rear element of the queue.  

    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else: raise IndexError("Queue is empty")


# Q7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.

    def size(self):
        if not self.is_empty():
            return self.item_count
        else: raise IndexError("Queue is empty")

myqueue = Queue()
try:
    print(myqueue.get_front())
except IndexError as e:
    print(e.args[0])
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
print("Front= ",myqueue.get_front(),", Rear= ",myqueue.get_rear(),", Size= ",myqueue.size())
try:
    myqueue.dequeue()
    myqueue.dequeue()
    print("Front= ",myqueue.get_front(),", Rear= ",myqueue.get_rear(),", Size= ",myqueue.size())
except IndexError as e:
    print(e.args[0])