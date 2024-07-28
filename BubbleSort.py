# Bubble Sort and Modified Bubble Sort

# Q1. Write a python function to implement bubble sort. 
def bubble(arr,n):
    for r in range(1,n):
        for i in range(n-r):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
arr=[5,2,4,3,1]
n=len(arr)
print(bubble(arr,n))


# Q2. Write a python function to implement modified bubble sort.

def mbubble(arr,n):
    Flag=0
    for r in range(1,n):
        Flag=0
        for i in range(n-r):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                Flag=1
        if Flag==0:
            break
    return arr

arr=[5,2,4,3,1]
n=len(arr)
print(mbubble(arr,n))
