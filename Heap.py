# Heap and Heap Sort 

# Q1. Define a class Heap to implement Heap data structure with __init__ method to create empty heap list. 

class Heap:
    def __init__(self):
        self.list=[]


# Q2. In class Heap, define a method to create a heap from a given list of element. 

    def create_heap(self,list):
        for i in list:
            self.insert(i)
        
    def heapify(self,i):
        n = len(self.list)
        largest=i
        left=2*i+1
        right=2*i+2
        if left<n and self.list[left]>self.list[largest]:
            largest=left
        if right<i and self.list[right]>self.list[largest]:
            largest=right
        if largest!=i:
            self.list[i],self.list[largest]=self.list[largest],self.list[i]
            self.heapify(largest)



# Q3. In class Heap, define a method insert to insert a given element in the heap at appropriate position. 

    def insert(self,i):
        n=len(self.list)
        p_index=(n-1)//2 
        while n>0 and self.list[p_index]<i:
            if n==len(self.list):
                self.list.append(self.list[p_index])
            else:
                self.list[n]=self.list[p_index]
            n=p_index
            p_index=(n-1)//2
        if n==len(self.list):
            self.list.append(i)
        else:
            self.list[n]=i


# Q4. In class Heap, define a top method which returns the top element of heap. Raise an exception if Heap is empty. 

    def top(self):
        if len(self.list) == 0:
            raise EmptyHeapException()
        return self.list[0]
    

# Q6. In class Heap, define a method delete which delete the top element and returns it. Raise an exception if Heap is empty. 

    def delete(self):
        if len(self.list) == 0:
            raise EmptyHeapException()
        if len(self.list) == 1:
            return self.list.pop()
        root = self.list[0]
        temp = self.list.pop()
        index=0 
        leftChild=2*index+1
        rightChild=2*index+2 
        while leftChild < len(self.list):
            if rightChild<len(self.list):
                if self.list[leftChild]>self.list[rightChild]:
                    if self.list[leftChild]>temp:
                        self.list[index]=self.list[leftChild]
                        index=leftChild
                    else:
                        break
                else:
                    if self.list[rightChild]>temp:
                        self.list[index]=self.list[rightChild]
                        index=rightChild 
                    else:
                        break 
            else:
                if self.list[leftChild]>temp:
                        self.list[index]=self.list[leftChild]
                        index=leftChild
                else:
                    break
            leftChild=2*index+1 
            rightChild=2*index+2
        self.list[index]=temp 
        return root
    

# Q7. In class Heap, define a method heapSort to sort a given list with help of heap.

    def heapSort(self,list1):
        self.create_heap(list1)
        list2=[]
        try: 
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2


# Q5. Define a class EmptyHeapException to describe custom exception.

class EmptyHeapException(Exception):
    def __init__(self,msg="Empty Heap"):
        self.msg=msg 
    def __str__(self):
        return self.msg


# Driver Code
list1=[40,70,10,90,60,30,50,20,80]
h=Heap()
list1=h.heapSort(list1)
print(list1)
