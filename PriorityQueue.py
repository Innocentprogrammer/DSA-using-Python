# Priority Queue Using List 

# Q1. Define a class PriorityQueue to implement priority queue data structure using list. Provide __init__() method to create a list object (inittally empty).

class PriorityQueue:
    def __init__(self):
        self.list=[]


# Q2. Define a push method in PriorityQueue class to insert new data with given priority.

    def push(self,priority,data):
        i=0
        while i<len(self.list) and self.list[i][0]<=priority:
            i+=1
        self.list.insert(i,(priority,data))


# Q3. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception in priority queue is empty.

    def pop(self):
        if not self.is_empty():
            return self.list.pop(0)[1]
        else:
            raise IndexError("Prioeity Queue is empty")


# Q4. Define a is_epmty method in PriorityQueue class to check if the priority queue is empty.

    def is_empty(self):
        return len(self.list)==0


# Q5. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.

    def size(self):
        if not self.is_empty():
            return len(self.list)
        else:
            raise IndexError("Prioeity Queue is empty")


#Driver Code:
pq=PriorityQueue()
pq.push(6,"G")
pq.push(5,"F")
pq.push(2,"C")
pq.push(0,"A")
pq.push(4,"E")
pq.push(3,"D")
pq.push(1,"B")
print(pq.list)
print("Size of Priority Queue: ",pq.size())
while not pq.is_empty():
    print("Remove Elements from Priority Queue: ",pq.pop())
try:
    print("Size of Priority Queue: ",pq.size())
except IndexError as e:
    print(e)
