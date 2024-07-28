# Selection Sort 

# Q1. Write a python function to implement selection sort. 

def selection(arr,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] <arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
arr = [7,1,5,2,3,8,4,6]
n = len(arr)
print(selection(arr,n))