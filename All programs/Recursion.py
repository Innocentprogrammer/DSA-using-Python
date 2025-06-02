# Q1. Write a recursion function to print first N natural numbers.

def f1(n):
    if n>0:
        f1(n-1)
        print(n,end=" ")
print("first 10 natural numbers: ")
f1(10)
print()


# Q2. Write a recursive function to print first N natural numbers in reverse order.

def f2(n):
    if n>0:
        print(n,end=" ")
        f2(n-1)
print("first 10 natural numbers in reverse order: ")
f2(10)
print()


# Q3. Write a recursive function to print first N odd natural numbers.

def f3(n):
    if(n>0):
        f3(n-1)
        print(2*n-1,end=" ")
print("first 10 odd natural numbers: ")
f3(10)
print()


# Q4. Write a recursive function to print first N even natural nubmers.

def f4(n):
    if(n>0):
        f4(n-1)
        print(2*n,end=" ")
print("first 10 even natural numbers: ")
f4(10)
print()


# Q5. Write a recursive function to print first N odd natural numbers in reverse order.

def f5(n):
    if(n>0):
        print(2*n-1,end=" ")
        f5(n-1)
print("first 10 odd natural numbers in reverse order: ")
f5(10)
print()


# Q6. Write a recursive function to print first N even natural nubmers in reverse order.

def f6(n):
    if(n>0):
        print(2*n,end=" ")
        f6(n-1)
print("first 10 even natural numbers in reverse order: ")
f6(10)
print()


# Q7. Write a recursive function to calculate sum of first N natural numbers. 

def f7(n):
    if n==1:
        return 1
    return n+f7(n-1)
print("sum of first 5 natural numbers: ",f7(5))


# Q8. Write a recursive function to calculate sum of first N odd natural numbers. 

def f8(n):
    if n==1:
        return 1
    return (2*n-1)+f8(n-1)
print("sum of first 5 odd natural numbers: ",f8(5))

# Q9. Write a recursive function to calculate sum of first N even natural numbers.

def f9(n):
    if n==1:
        return 2
    return (2*n)+f9(n-1)
print("sum of first 5 even natural numbers: ",f9(5))


# Q10. Write a recursive function to calculate factorial of a number.

def f10(n):
    if n==1:
        return 1 
    return n*f10(n-1)
print("factorial of 5: ",f10(5))


# Q11. Write a recursive function to calculate sum of square of first N natural numbers.

def f11(n):
    if n==1:
        return 1 
    return pow(n,2)+f11(n-1)
print("sum of square of first 5 natural numbers: ",f11(5))