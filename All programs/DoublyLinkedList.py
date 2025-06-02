# Q1 Define a class Node to describe a node of Doubly linked list.

class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


# Q2 Define a class DLL to implement Doubly Linked List with __init__() method to create and initialise start reference variable

class DLL: 
    def __init__(self, start=None):
        self.start = start


# Q3 Define a method is_empty() to check if linked list is empty in DLL class.

    def is_empty(self):
        return self.start == None


# Q4 In class DLL, define a method insert_at_start() to insert an element at the starting of the list.

    def insert_at_start(self,data):
        new_node = Node(None,data, self.start)
        if not self.is_empty():
            self.start.prev=new_node
        self.start=new_node


# Q5 In class DLL, define a method insert_at_last() to insert an element at the end of the list.

    def insert_at_end(self,data):
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
        new_node=Node(temp,data,None)
        temp.next=new_node
        if temp==None:
            self.start=new_node
        else:
            temp.next=new_node


# Q6 In class DLL, define a method search() to search an node with specified element value.

    def search(self,data):
        temp=self.start     
        while temp.next is not None:
            if temp.data==data:
                return temp
            temp=temp.next
        return None


# Q7 In class DLL, define a method insert_after() to insert new node after a given node of the list.

    def insert_after(self,temp,data):
        if temp is not None:
            new_node=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=new_node
            temp.next=new_node


# Q8 In class DLL, define a method to print all the element of list.
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next


# Q9 In class DLL, define a method delete_first() to delete first element from the list.

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            self.start.next.prev=None


#  Q10 In class DLL, define a method delete_last() to delete last element from the list.
  
    def delete_last(self):
        if self.start.next is None:
            self.start = None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    

# Q11 In class DLL, define a method delete_item() to delete specified element from the list.

    def delete_item(self,data):
        if self.start.next is None:
            if self.start.data==data:
                self.start=None
        else:
            temp=self.start
            if temp.data==data:
                self.start=temp.next
                temp.next.prev=None
            else:
                while temp.next is not None:
                    if temp.next.data==data:
                        temp.next=temp.next.next
                        temp.next.next.prev=temp
                        break
                    temp=temp.next


# Q12 In class DLL, implement iterator for DLL to access all the elements of the list in a sequence.

    def __iter__(self):
        return DLLIterator(self.start)

class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next 
        return data


#Driver Code
mylist=DLL()
mylist.insert_at_start(2)
mylist.insert_at_start(1)
mylist.insert_at_end(3)
mylist.insert_at_end(6)
mylist.insert_after(mylist.search(3),4)
mylist.insert_after(mylist.search(4),5)
mylist.print_list()
mylist.delete_first()
mylist.delete_last()
mylist.delete_item(3)
print()

# for iterator
for i in mylist:
    print(i,end=" ")
print()
# for direct
mylist.print_list()