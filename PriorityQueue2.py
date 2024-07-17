# Priority Queue Using Doubly Linked List

# Q1. Define a Node class with instance member variables item, priority and next.

class Node:
    def __init__(self,priority=None,data=None,next=None):
        self.priority = priority
        self.data = data
        self.next = next


# Q2. Define a class PriorityQueue to implement priority queue data structure using singly linked list. Provide __init__() method to create a start reference variable (initially containing None) and item_count variable (initially 0).

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0


# Q3. Define a push method in PriorityQueue class to insert new data with given priority.

    def push(self,priority,data):
        new_node = Node(priority,data)
        if self.start is None:
            new_node.next=None 
            self.start=new_node
        else:
            if self.start!=None and self.start.priority>priority:
                new_node.next=self.start 
                self.start=new_node
            else:
                temp=self.start
                while temp.next.next!=None :
                    if temp.next.priority>=priority:
                        new_node.next=temp.next
                        temp.next=new_node
                        break
                    temp=temp.next
                if temp.next.priority<priority:
                    temp.next.next=new_node
        self.item_count+=1
                

# Q4. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.

    def pop(self):
        if not self.is_empty():
            print("Remove element form Priority Queue: ",self.start.data)
            self.start=self.start.next 
        else:
            raise Exception("Priority Queue is empty")
        self.item_count-=1


# Q5. Define a is_empty method in PriorityQueue class to check if priority queue is empty. 

    def is_empty(self):
        return self.start==None


# Q6. In class PriorityQueue, define a method size to return the number of elements present in priority queue.

    def size(self):
        return self.item_count
    
#Driver Code:
pq=PriorityQueue()
pq.push(5,"F")
pq.push(4,"E")
pq.push(1,"B")
pq.push(3,"D")
pq.push(2,"C")
pq.push(0,"A")
pq.push(6,"G")
pq.push(7,"H")
print("Size of Priority Queue: ",pq.size())
while not pq.is_empty():
    pq.pop()
print("Size of Priority Queue: ",pq.size())

