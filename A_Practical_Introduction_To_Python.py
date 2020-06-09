class Student: #student class

  perc_rise = 1.05

  def __init__(self, first, last, marks): #initialize our instances or constructor
    self.first = first
    self.last = last
    self.marks = marks
    self.email = first + '.' + last + '@gmail.com'

  def fullname(self): #funtion to print the fullname

    return '{} {}'.format(self.first, self.last)

  def apply_rise(self):
    self.marks = int(self.marks * 1.05)

    
#CLASS INHERITANCE
class Dumb(Student): #Creating a subclass inheritance from the student class

  perc_rise = 1.10  #percent raise in the Dumb class

  def __init__(self, first, last, marks, prog_lang): # define an init function for the Dumb class
    super().__init__(first , last, marks) # inherit from the student class
    self.prog_lang = prog_lang #initialize the prog_lang

Std_1 = Dumb('ibrahim', 'suleiman', 60,'python')#creating an object for student 1
#Std_2 = Student('khalil', 'ibrahim', 90)#creating an object for strudent 2

print(Std_1.prog_lang)

#print(Std_1.perc_rise)

#print(help(Dumb))
#Std_2.apply_rise()
#print(Student.__dict__)
#print(Std_1.fullname())
#print(Std_2.fullname())

#python inheritance
#inheritance allows us to define a class that inherits all the methods and properties from another class.
#parent class and child class
class Person:

  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#use the person class to create an object, and then execute the printname method:
x = Person('ibrahim', 'suleiman')
x.printname()

#child class
#create a student class that will inherit properties from the person class

class Student(Person):

  pass
#use the student class to create an object and then execute the printname method
x = Student('khalil', 'excel')
x.printname()

""" Add the __init__() function so far we have created a child class that inherits the properties and methods from its parent
we want to add the __init__()function to the child class of the pass keyword
"""
class Student(Person):

  def __init__(self, fname, lname):

    pass

    #Add properties etc
"""
when you add the __init__() function, the child class will no longer inherit the parents __init__() function
note the childs __init__function overrides the inheritance of the parents __init__() function
"""
class Student(Person):
  def __init__(self, fname, lname):

    Person.__init__(self, fname, lname)

"""
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready
to add functionality in the __init__() function

USe the super()function python also has a super() function that will make the child class inherit all the methods and properties from parent

"""
class Student(Person):

  def __init__(self, fname, lname):

    super().__init__(fname, lname)

"""
by using the super() function you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent
Add properties
example add a property called graduationyear to the Student class:
"""
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#In the example below, the year 2019 should be a variable, and passed into the Student class when creating objects. to do so add another parameter in the __init__() function:
#example: add a year parameter, and pass the correct year when creating objects:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student('ibrahim', 'suleiman', 2016)


#Add methods

"""
Abstract Classes in Python
An abstract class can be considered as a blueprint for other classes, allows you to create
a set of methods that must be created within any child classes built from your abstract class
a class which contains one or abstract methods is called an abstract class.

An abstract method is a method that has declaration but not has any implementation.

How Abstract Base classes work
"""

#code 1: Python program showing abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

  #abstract method
  def no_of_sides(self):

    pass

class Triangle(Polygon):

  #overriding abstract method
  def no_of_sides(self):

    print("i have 3 sides")

class pentagon(Polygon):

  #overriding abstract method
  def no_of_sides(self):

    print("I have 5 sides")

class hexagon(Polygon):

  #overriding abstract method

  def no_of_sides(self):

    print("I have 6 sides")

class Quadrilateral(Polygon):

  #overriding abstract method

  def no_of_sides(self):

    print("I have 4 sides")

#driver code
R = Triangle()
R.no_of_sides()

K = pentagon()
K.no_of_sides()

M = hexagon()
M.no_of_sides()

Q = Quadrilateral()
Q.no_of_sides()

#code 2: python program showing abstract base class work

from abc import ABC, abstractmethod

class Animal(ABC):

  def move(self):

    pass

class ibrahim(Animal):

  def move(self):

    print("I can walk")

class sheep(Animal):

  def move(self):

    print("I can walk with my four legs")

class snake(Animal):

  def move(self):

    print("I can crawl")

class Bird(Animal):

  def move(self):

    print("I can fly")


I = ibrahim()
I.move()

s = sheep()
s.move()

S = snake()
S.move()

B = Bird()
B.move()

#implementation through subclassing: by subclassing directly from the base, we can avoid the need to register the class
#explicitly. in this case, the python class management is used to recognize pluginImplementation as implementing the abstract PluginBase.
#python program showing implementation of abstract class through subclasssing

import abc

class parent:

  def geeks(self):

    pass

class child(parent):

  def geeks(self):

    print("child class")

print(issubclass(child,parent))
print(isinstance(child(), parent))

#ABSTRACT CLASS
from abc import ABC, abstractmethod  #import the abstract class

class Employee(ABC): #the class employee inherit from the abstract class ABC

  @abstractmethod #decoration for the abstract method

  def calculate_salary(self, sal): #define an abstract method

    pass

class Developer(Employee):

  def calculate_salary(self, sal):

    finalsalary = sal * 1.10

    return finalsalary

emp_1 = Developer()
print(emp_1.calculate_salary(10000))

#python program to demonstrate instantiating a class

class Dog:
  #a simple class attribute
  attr1 = 'mamal'
  attr2 = 'dog'

  # a sample method
  def disp(self):
    print('I am a', self.attr1)
    print('I am a', self.attr2)

#Driver code object instantiation
billy = Dog()

#Accessing class attributes and method through objects
print(billy.attr1)
billy.disp()

# The __init__ method
class Person:

  #init method or constructor
  def __init__(self, name):
    self.name = name

  #sample method
  def say_hi(self):
    print('hello my name is', self.name)

p = Person('ibrahim')
p.say_hi()

#Class and Instance variable
#Python program to show that the variables with a assigned in class declaration, are class variables and
#variables inside methods and constructors are instance variables

#class for computer science
class Dog:

  #class variable
  animal = 'dog'

  #The init method or constructor
  def __init__(self, breed, color):

    #instance variable
    self.breed = breed
    self.color = color

#objects of CSStudent class
Rodger = Dog("pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a',Rodger.animal)
print('Breed:',Rodger.breed)
print('Color:',Rodger.color)

print('\nBuzo details:')
print('Buzo is a',Buzo.animal)
print('Breed:',Buzo.breed)
print('color:',Buzo.color)

#class variables can be assessed using class names also
print('\nAccessing class variable using class name')
print(Dog.animal)
 
#defining instance variable using normal method
#python program to show that we can create instance variable inside methods

#class for computer science students
class Dog:

  #class variable
  animal = 'dog'

  #the init method or constructor
  def __init__(self, breed):

    #instance variable
    self.breed = breed

  #Adds an instance variable
  def setColour(self, colour):
    self.colour = colour

  #Retrieves instance variable
  def getColour(self):
    return self.colour

#Driver code
Rodger = Dog('pug')
Rodger.setColour('brown')
print(Rodger.getColour())

full_name = input("enter your full name")
favourite_color = input("enter your favourite color")
print(full_name + "likes"+ favourite_color)
full_name.capitalize() 
