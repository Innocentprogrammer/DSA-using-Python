# Q1 Define a python class Person with instance object variables name and age. Set Instance object variables in __init__() nethod. Also define show() method to display name and age of a person.

class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def setter(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

p1=Person()
p1.setter('John', 23)
p1.show()


# Q2 Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.

class Circle:
    def __init__(self, radius=None):
        self.radius=radius
    def setter(self, radius):
        self.radius=radius
    def getter(self):
        return self.radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius

c1=Circle()
c1.setter(10)
print("Radius: ",c1.getter())
print("Area: ",c1.getArea())
print("Circumference: ",c1.getCircumference())


# Q3 Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions() and getArea() method in it.

class Rectangle:
    def __init__(self, length=None, breadth=None):
        self.length=length
        self.breadth=breadth
    def setDimensions(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def showDimensions(self):
        print("Length: ",self.length)
        print("Breadth: ",self.breadth)
    def getArea(self):
        return self.length*self.breadth

r=Rectangle()
r.setDimensions(10,20)
r.showDimensions()
print("Area: ",r.getArea())


# Q4 Define a class Book with instance object variables bookid, title, and price. Initialise them via __init__() method. Also define method to show book variables.

class Book:
    def __init__(self, bookid=None, title=None, price=None):
        self.bookid=bookid
        self.title=title
        self.price=price
    def showBooks(self):
        print("Book Id: ",self.bookid)
        print("Title: ",self.title)
        print("Price: ",self.price)

b1=Book(121, 'Power of Money', 550.00)
b2=Book(132, '7 Habits', 200.00)
b3=Book(434, 'Rich Dad Poor Dad', 899.00)
b1.showBooks()
b2.showBooks()
b3.showBooks()


# Q5 Define a class Team with instance object variable a list of team member names. Provide methods to input member names and display member names.

class Team:
    def __init__(self):
        self.name=[]
    def inputName(self):
        while True:
            member = input("Enter a Team member names(or 'e' for exit): ")
            if member.lower()=='e':
                break
            else:
                self.name.append(member)
    def display_member(self):
        if not self.name:
            print("No team member found")
        else:
            print("Team members are:")
            print(f"{self.name}")
        
t=Team()
t.inputName()
t.display_member() 
