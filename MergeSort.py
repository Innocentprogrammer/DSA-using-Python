# Merge Sort 

# Q1. Write a python function to implement merge sort. 

def merge(arr):
    if len(arr)>1:
        mid = (len(arr))//2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr
    
arr=[7,1,2,3,8,4,6,5]
print(merge(arr)) 

