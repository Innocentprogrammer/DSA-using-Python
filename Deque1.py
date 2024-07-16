# Deque Using List 

# Q1. Define a class Deque to implement deque data structure using list. Define __init__() method to create an empty list object as instance object member of Deque.

class Deque:
    def __init__(self):
        self.list = []


# Q2. Define a method is_empty() to check if deque is empty in Deque class.

    def is_empty(self):
        return len(self.list) == 0


# Q3. In Deque class, define insert_front() method to add data at front end of the deque.

    def insert_front(self,data):
        self.list.insert(0,data)
        print(self.list)


# Q4. In Deque class, define insert_rear() method to add data at rear end of the deque.

    def insert_rear(self,data):
        self.list.append(data)
        print(self.list)


# Q5. In Deque class, define delete_front() method to remove front element from the deque.

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.list.pop(0)


# Q6. In Deque class, define delete_rear() method to remove rear element from the deque.

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.list.pop()


# Q7. In Deque class, define get_front() method to return front element from the deque.

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.list[0]


# Q8. In Deque class, define get_rear() method to return rear element from the deque.

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.list[-1]


# Q9. In Deque class, define size() method to return size of the deque that is number of items present in deque.

    def size(self):
        if self.is_empty():
            return 0
        else:
            return len(self.list)


#Driver Code:
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