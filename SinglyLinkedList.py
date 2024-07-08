# Q1 Define a class Node to describe a node of singly linked list.

class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next


# Q2 Define a class SLL to implement Singly Linked List with __init__() method to create and initialise start reference variable

class SLL:
    def __init__(self, head=None):
        self.head=head


# Q3 Define a method is_empty() to check if linked list is empty in SLL class.

    def is_empty(self):
        return self.head==None


# Q4 In class SLL, define a method insert_at_start() to insert an element at the starting of the list.

    def insert_at_start(self,item):
        newNode=Node(item,self.head)
        self.head=newNode


# Q5 In class SLL, define a method insert_at_last() to insert an element at the end of the list.

    def insert_at_last(self,item):
        newNode=Node(item)
        if not self.is_empty():
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
        else:
            self.head=newNode
    

# Q6 In class SLL, define a method search() to search an node with specified element value.

    def search(self,item):
        temp=self.head
        while temp!=None:
            if temp.item==item:
                return temp
            temp=temp.next
        return None
    

# Q7 In class SLL, define a method insert_after() to insert new node after a given node of the list.

    def insert_after(self,temp,item):
        if temp is not None:
            newNode=Node(item,temp.next)
            temp.next=newNode


# Q8 In class SLL, define a method to print all the element of list.

    def print_LL(self):
        temp=self.head
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next


# Q9 In class SLL, define a method delete_first() to delete first element from the list.

    def delete_first(self):
        if self.head is not None:
            self.head=self.head.next
    

# Q10 In class SLL, define a method delete_last() to delete last element from the list.

    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    

# Q11 In class SLL, define a method delete_item() to delete specified element from the list.

    def delete_item(self,item):
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.item==item:
                self.head=None
        else:
            temp=self.head
            if temp.item == item:
                self.head=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == item:
                        temp.next=temp.next.next
                        break
                    temp=temp.next 


# Q12 In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.

    def __iter__(self):
        return SLLIterator(self.head)


class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        item=self.current.item
        self.current=self.current.next 
        return item


#driver code

head=SLL()
head.insert_at_start(2)
head.insert_at_last(4)
head.insert_at_start(1)
head.insert_after(head.search(2),3)
head.insert_at_last(5)
head.insert_at_last(6)
head.insert_at_last(7)
head.insert_at_start(0)
head.delete_first()
head.delete_last()
head.delete_item(4)

#for iterator
for i in head:
    print(i,end=' ')
#for direct 
head.print_LL()
