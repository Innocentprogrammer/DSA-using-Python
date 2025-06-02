# Quick Sort 

# Q1. Write a python function to implement quick sort. 

def Quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    less=[]
    greate=[]
    for i in arr[1:]:
        if i<=pivot:
            less.append(i)
        else:
            greate.append(i)
    return Quick(less)+[pivot]+Quick(greate)
arr=[7,1,2,3,8,4,6,5]
print(Quick(arr)) 
