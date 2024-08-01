# Searching 

# Q1. Write a python function to implement Linear Search. 

def Linear(arr):
    target = int(input("Enter the target element: "))
    for i in range(len(arr)):
        if arr[i] == target:
            return i+1
    return -1


# Q2. Write a python function to implement Binary Search. 

def Quick(arr):
    if len(arr)>1:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x> pivot]
        return Quick(less) + [pivot] + Quick(greater)
    else:
        return arr

def Binary(arr,target,low,high):
    sorted_arr=Quick(arr)
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid+1
        elif sorted_arr[mid] < target:
            low = mid + 1
            return Binary(sorted_arr,target,low,high)
        else:
            high = mid - 1
            return Binary(sorted_arr,target,low,high)
    return -1

arr=[7,2,3,1,4,6,5,8,10]
print("location of target: ",Linear(arr))
target=int(input("Enter the target element: "))
print("location of target: ",Binary(arr,target,0,len(arr)))

