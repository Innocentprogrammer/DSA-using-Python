## Insertion Sort

# Q1. Write a python function to implement Insertion sort

def insertion(arr):
    for i in range(1, len(arr)):
        curr=arr[i]
        pos=i
        for j in range(i-1,-1,-1):
            if curr<arr[j]:
                arr[j+1]=arr[j]
                pos=j
        arr[pos]=curr
    return arr
arr = [7,1,5,2,3,8,4,6]
print(insertion(arr))
