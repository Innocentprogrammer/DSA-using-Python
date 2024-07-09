# Q1. Define a class Node to describe a node of Circular doubly linked list.
class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev=prev 
        self.data=data
        self.next=next 


# Q2. Define a class CDLL to implement Circular Doubly Linked List with __init__() method to create and initialise start reference variable

class CDLL:
    def __init__(self, start=None):
        self.start=start


# Q3. Define a method is_empty() to check if linked list is empty in CDLL class.

    def is_empty(self):
        return self.start==None


# Q4. In class CDLL, define a method insert_at_start() to insert an element at the starting of the list.

    def insert_at_start(self,data):
        # newNode=Node(data)
        # if self.is_empty():
        #     newNode=Node(newNode,data,newNode)
        # else:
        #     newNode=Node(self.start.prev, data, self.start)
        #     self.start.prev.next=newNode
        #     self.start.prev=newNode
        # self.start=newNode
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n  


# Q5. In class CDLL, define a method insert_at_last() to insert an element at the end of the list.

    def insert_at_last(self,data):
        # newNode=Node(data)
        # if self.is_empty():
        #     newNode=Node(newNode,data,newNode)
        #     self.start=newNode
        # else:
        #     newNode=Node(self.start.prev,data,self.start)
        #     self.start.prev.next=newNode
        #     self.start.prev=newNode
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n 
        else:
            n.next=self.start   
            n.prev=self.start.prev
            n.prev.next=n
            self.start.prev=n
        

# Q6. In class CDLL, define a method search() to search an node with specified element value.

    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.data==data:
            return temp
        else:
            temp=temp.next
        while temp != self.start:
            if temp.data==data:
                return temp
            temp=temp.next 
        return None 
    
        
# Q7. In class CDLL, define a method insert_after() to insert new node after a given node of the list.

    def insert_after(self,temp,data):
        # if temp is not None:
        #     newNode=Node(temp,data,temp.next)
        #     temp.next.prev=newNode
        #     temp.next=newNode
        #     if temp == self.start:
        #         self.start=newNode
        if temp is not None:
            n=Node(data)
            n.next=temp.next 
            n.prev=temp
            temp.next.prev=n
            temp.next=n


# Q8. In class CDLL, define a method to print all the element of list.

    def printCDLL(self):
        # temp=self.start 
        # while temp.next != self.start:
        #     print(temp.data, end=" ")
        #     temp=temp.next
        temp=self.start 
        if temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.data, end=" ")
                temp = temp.next


# Q9. In class CDLL, define a method delete_first() to delete first element from the list.

    def delete_first(self):
        # if self.start == self.start.prev:
        #     self.start=None
        # else:
        #     self.start.prev.next=self.start.next 
        #     self.start.next.prev=self.start.prev
        #     self.start=self.start.next
        if self.start is not None:
            if self.start.next == self.start:
                self.start=None 
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next


# Q10. In class CDLL, define a method delete_last() to delete last element from the list.

    def delete_last(self):
        # if self.start == self.start.prev:
        #     self.start=None
        # else:
        #     self.start.prev.prev.next=self.start 
        #     self.start.prev=self.start.prev.prev
        if self.start is not None:
            if self.start.next == self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start 
                self.start.prev=self.start.prev.prev 


# Q11. In class CDLL, define a method delete_item() to delete specified element from the list.

    def delete_Item(self,data):
        # if self.start == self.start.prev:
        #     if self.start.data == data:
        #         self.start=None
        # if self.start.next.prev==self.start:
        #     if self.start.data == data:
        #         self.start.prev=self.start
        #         self.start.next=self.start
        # else:
        #     temp=self.start
        #     while temp.next != self.start:
        #         if temp.data == data:
        #             temp.prev.next=temp.next
        #             temp.next.prev=temp.prev
        #         temp=temp.next
        if self.start is not None:
            temp = self.start 
            if temp.data==data:
                self.delete_first()
            else:
                temp=temp.next 
                while temp is not self.start:
                    if temp.data==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next


# Q12. In class CDLL, implement iterator for CDLL to access all the elements of the list in a sequence.

    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start 
        self.count=0
    def __iter__(self):
        return self 
    def __next__(self):
        if self.current is None:
            return StopIteration
        if self.current == self.start and self.count == 1:
            return StopIteration
        else: 
            self.count = 1
        data=self.current.data 
        self.current=self.current.next 
        return data


#Driver Code
mylist=CDLL()
mylist.insert_at_start(3)
mylist.insert_at_start(2)
mylist.insert_at_start(1)
mylist.insert_after(mylist.search(3),4)
mylist.insert_after(mylist.search(4),5)
mylist.insert_at_last(6)
mylist.insert_at_last(7)
mylist.printCDLL()
mylist.delete_first()
mylist.delete_last()
mylist.delete_Item(4)
print()
mylist.printCDLL()