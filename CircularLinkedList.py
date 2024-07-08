# Q1. Define a class Node to describe a node of Circular linked list.

class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next


# Q2. Define a class CLL to implement Circular Linked List with __init__() method to create and initialise start reference variable

class CLL:
    def __init__(self, last=None):
        self.last=last


# Q3. Define a method is_empty() to check if linked list is empty in CLL class.

    def is_empty(self):
        return self.last==None


# Q4. In class CLL, define a method insert_at_start() to insert an element at the starting of the list.

    def inser_at_start(self,item):
        newNode=Node(item)
        if self.is_empty():
            newNode.next=newNode
            self.last=newNode
        else:
            newNode.next=self.last.next
            self.last.next=newNode


# Q5. In class CLL, define a method insert_at_last() to insert an element at the end of the list.

    def insert_at_last(self,item):
        newNode=Node(item)
        if self.is_empty():
            newNode.next=newNode
            self.last=newNode
        else:
            newNode.next=self.last.next
            self.last.next=newNode
            self.last=newNode


# Q6. In class CLL, define a method search() to search an node with specified element value.

    def search(self,item):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp != self.last:
            if temp.item==item:
                return temp
            temp=temp.next
        if temp.item == item:
            return temp
        return None
    

# Q7. In class CLL, define a method insert_after() to insert new node after a given node of the list.

    def insert_after(self,temp,item):
        if temp is not None:
            newNode=Node(item,temp.next)
            temp.next=newNode
            if temp == self.last:
                self.last=newNode


# Q8. In class CLL, define a method to print all the element of list.

    def print_CLL(self):
        temp = self.last.next 
        while temp != self.last:
            print(temp.item,end=" ")
            temp=temp.next
        print(temp.item)

# Q9. In class CLL, define a method delete_first() to delete first element from the list.

    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            self.last.next=self.last.next.next


# Q10. In class CLL, define a method delete_last() to delete last element from the list.

    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            temp=self.last.next
            while temp.next != self.last:
                temp=temp.next 
            temp.next=self.last.next
            self.last=temp


# Q11. In class CLL, define a method delete_item() to delete specified element from the list.

    def delete_item(self,item):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==item:
                    self.last=None
            else:
                if self.last.next.item==item:
                    self.delete_first()
                else:
                    temp=self.last.next
                    while temp!= self.last:
                        if temp.next==self.last:
                            if self.last.item==item:
                                self.delete_last()
                                break
                        if temp.next.item==item:
                            temp.next=temp.next.next 
                            break
                        temp=temp.next 

# Q12. In class CLL, implement iterator for CLL to access all the elements of the list in a sequence.

    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
    
class CLLIterator:
    def __init__(self,start):
        self.current=start 
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        item=self.current.item
        self.current=self.current.next
        return item


#Driver Code
mylist=CLL()
mylist.inser_at_start(2)
mylist.inser_at_start(1)
mylist.insert_after(mylist.search(2),3)
mylist.insert_after(mylist.search(3),4)
mylist.insert_at_last(5)
mylist.insert_at_last(6)
mylist.insert_at_last(7)
mylist.print_CLL()
mylist.delete_first()
mylist.delete_last()
mylist.delete_item(4)
for i in mylist:
    print(i,end=" ")
