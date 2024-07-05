# Q1 Given an array with some integer type values. Write a python script to sort array values.

from array import *
a1=array('i',[3,2,4,0,9,1])
print(sorted(a1))

# Q2 Given a list of heterogenous elements. Write a python script to remove all the non int values from the list.

l1=[1,2,'a',5.3,4.9,'b',4]
l2=[]
for i in l1:
    if(type(i)==int):
        l2.append(i)
print(l2)

# Q3 Write a Python script to calculate average of element of a list.

l1=[3,2,4,0,9,1]
sum=0
for i in l1:
    sum+=i
average=sum/(len(l1))
print(average)

# Q4 Write a Python script to create a list of first N prime numbers.

N=int(input())
l1=[]
for i in range(2,N+1):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        l1.append(i)
print(l1)

# Q5 Write a Python script to create a list of first N terms of a Fibonacci series.

N=int(input())
a=0
b=1
print(a,b,end=' ')
for i in range(2,N):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
