# Queue Using List

# Q1. Define a class Queue to implement queue data structure using list. Define __init__() method to create an empty list object as instance object member of Queue.

class Queue:
    def __init__(self):
        self.list=[]


# Q2. Define a method is_empty() to check if the queue is empty in Queue class.

    def is_empty(self):
        return len(self.list)==0


# Q3. In Queue class, define enqueue() method to add data at the rear end of the queue.

    def enqueue(self,data):
        self.list.append(data)
        print(self.list)


# Q4. In Queue class, define dequeue() method to remove front element from the queue.

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.list.pop(0)


# Q5. In Queue class, define get_front() method to return front element of the queue.

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.list[0]


# Q6. In Queue class, define get_rear() method to return rear element of the queue.

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.list[-1]


# Q7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.

    def size(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return len(self.list)


#Driver Code
myqueue=Queue()
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
myqueue.enqueue(6)
print("Front element of Queue: ",myqueue.get_front())
print("Rear element of Queue: ",myqueue.get_rear())
print("Total no. of element in Queue: ",myqueue.size())
print("Removed element from front side of Queue: ",myqueue.dequeue())
print("Removed element from front side of Queue: ",myqueue.dequeue())
print("Front element of Queue: ",myqueue.get_front())
print("Rear element of Queue: ",myqueue.get_rear())
print("Total no. of element in Queue: ",myqueue.size())
