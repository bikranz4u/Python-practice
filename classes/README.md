welcome to Object Oriented Prog using Python Training.


1) In Brief about your current profile
2) Experience with python 
3) have you attended the Python Beyond Basics or others trngs
4) Why ?


Day1:-
------
Ramp-up
Classes

Day2:-
------
Classes - leftover
Iterator
Decorator
GEnerator
Intro to some design patterns
Other topics



>> Write u r own classes
>> modify classes
>> Think towards OOP
>> design OOP
>> develop API 


>>fundamentals of python
>>OOPs


Revist:-
========
I/o          :  print("Hello world %s" %(name))
                res = input("enter the value : ")

str          :  index    : first - arr[0]
                           last  - arr[-1]

                slicing  : first4        - arr[:4]
                           except first4 - arr[4:] 
                           last4         - arr[-4:]
                           except last4  - arr[:-4]
                           alternate     - arr[::2]/arr[1::2]
                           reverse       - arr[::-1]	
                split    : flst  = data.split(DELIMITER)
                join     : res = "DELIMITER".join(STRLIST)
                trim     : data.strip()/lstrip()/rstrip()

list comp    :  data=["10" , "20", "30", "40"]
                res = [int(elem) for elem in data ]
                res = [int(elem) for elem in data  elem.isdigit()]

tuple        :  1) a,b,c = 10,20,30
                2) a,b  = b,a
                3) *a,b,c = 10,20,30,40,50,60
                   a,*b,c = 10,20,30,40,50,60
                   a,b,*c = 10,20,30,40,50,60
                  
list         :  empty list  - arr=[]
                expand      - arr.append(ITEM)
                shrink      - arr.pop(INDEX) /arr.remove(ITEM) 
                sort        - arr.sort()
                reverse     - arr.reverse()

set          :  empty set   - grp1=set()
                union       - res = grp1|grp2
                intersection- res = grp1&grp2
                diff        - res = grp1-grp2
                sym diff    - res = grp1^grp2

dict         :  empty dict  - atab={}
                expand      - atab["kar"] = "blr" # add/modify
                shrink      - atab.pop("kar")

files        :  f1 = open("data.txt", "w")
                f1.write("alpha\n")
                f1.write("beta\n")
                f1.write("delta\n")
                f1.write("omega")
                f1.close() 
                 
                with open("data.txt", "r") as fob:
                     for elem in fob:
                          elem = elem.rstrip("\n")
                          print(elem)     

functions    : def express(op1,op2,oper,out): - compulsory args
                                              - positional args

               def express(op1=1,op2=1,oper="add",out="console"):
                                             - default args
                                             - optional args

               def express(op1,op2,oper="add",out="console"):
                                             - Hybrid args
 
               pure functs  - which accepts args & Returns


def compare(file1,file2):
   some state
   return True

fnname          =  compare
no of args      =  2
type of args    =  string, string
type of fn      =  compulsory
is it a pure fn =  yes


def merge(alst,blst,clst):
  some state
  
fnname          =  merge
no of args      =  3
type of args    =  list,list,list
type of fn      =  compulsory
is it a pure fn =  no


def get_key(atab):
  some state
  return flag

fnname          =  get_key
no of args      =  1
type of args    =  dict
type of fn      =  compulsory
is it a pure fn =  yes


def power(num=2,raised=1):
  some
  return res

fnname          =  power
no of args      =  2
type of args    =  int, int
type of fn      =  default
is it a pure fn =  yes



modules      :

             fully qualified name = worldmap.asia.india.kar.blr

             relative name        = india.kar.blr
                                  = kar.blr
                                  = blr


             Assume we have a lib named "mathlib.py"
             add(a,b)/minus(a=0,b=0)/divide(a,b=5)/mult()    

             1) import mathlib        # FQN

                mathlib.add(10,20)    

             2) import mathlib as m   # aliasing  - FQN

                m.minus()

             3) from mathlib import *  # REL NAMES

                divide(10)   
               
             4) from mathlib import mult #selective - REL
                
                mult()  


--------------------------------------------------------------------------
Mr. Raghu requires 

-corpus of 6lakhs
-time 3 years
-save upto - 10 per month


4 lakhs
 

>>Increase the savings
>>start invest this stock 
>>start working extra



Problem Solving:-
-----------------

Top Down  - start execution
          - design 
          - start execution
          - re-design
          - procedural lang/modular lang/imperative lang


Bottom up - clear STOP & clear START
          - design classes
          - define execution
          - Object Oriented Lang  - C++/JAva/C# 


Object Oriented Concepts:-
===========================
Abstraction        - generalization
Encapsulation      - create instance
Data hiding        - private
Inheritance        - specialization class
Polymorphism       - specialization method


Entity       - Noun
Attributes   - properties     - DATA
Behaviours   - functionality  - FUNCTIONS


Mobile - Entity
Attrs  - screensize
         os
         ram
         internalmem
         apps
behvrs - call()
         recv()
         sendsms()




Cricket match:-
===============
>> Team
>> Players
>> umpire
>> coach
>> audie


batsman  - name, age, team, runrate, best
bowler   - name, age, team, wkts, avg
fielder  - name, age, team, catches, runouts 
wkeeper  - name, age, team, stumps, catchtes 
captian  - name, age, team, won, lost
vcap     - name, age, team, captian, won, lost


Generalize the ROLES - Player ( GENERALIZATION )
collect common attributes - name, age, team
collect common bhevrs     - field(), score(), play()


 
Specialization:-
=================
                       Player
                         |
             --------------------------
            Bowler                    Batsman
              |                          |
     ------------------------        
   Spin        medium       Fast        RHB  LHB    
    



Design Phase            Implementation
--------------          --------------
GEneral entity          CLASS
Entity                  Object
attributes              data members
behaviours              methods




which are not a part of class - functions
                              - can be called directly

which are part of a class     - methods
                              - can be called only via objects


==============================================================================
class   - Design 
        - defined rules & regulations
        - does't have memory footprints
    
object  - implementation
        - follow the rules & regulations
        - have memory footprints


==============================================================================
Table driven thinking:-
=======================

Class       -  TABLENAME
object      -  EACH ROW in a table 
data member -  COLUMN LABLES
methods     -  OPERATIONS on each row
mutator     -  is a method - write on data members
non-mutator -  is a method - readonly data members
predicate   -  is a method - return True/False

How to create a object  - objref = Classname()
message passing         - objref.methodname()


Note:
  python memory allocation - DYNAMIC MEMORY ALLOCATION
                           - we don't have a keyword - "new"
 
Note:
  res = callme()   # is it function-call     - YES
                     is it Object Creation 

  res = Person()    # is it function-call
                     is it Object Creation  - YES


Step-1 :  problem
Step-2 :  identify the entities in a problem
step-3 :  identify the attrbutes & behaviours
step-4 :  generalize - common attr & common bhevrs
step-5 :  we write a CLASS



                       Classes
                          |
           --------------------------------
          |                                |
   Compile Time                      Run Time Classes

 we develop in C++/JAVA/C#           we develop in Python 
 we define data members              we DON'T define data members
 we define methods                   we define methods
 "this" pointer                      "self" reference      
 define a method-"this" is IMPLICIT  "self" pointer EXPLICIT
 CTOR - samename as class name       def __init__(self)
 DTOR - optional                     optional since we have GC

 supports over-loading               does't support overloading

 inheritance supported               inheritance supported
 has ctor cascading                  does't have ctor cascading
 does't support MI                   supports Multiple Inheritance

 supports over-riding                support for over-riding


Python Class Developement:-
============================
1) we are developing RUN TIME Classes
2) we have a feature - MONKEY PATCHING
3) Type checking     - Duck Typing

4) Class hierarchy   - object
5) "this" pointer    - "self" - it is not keyword-naming convention
6) default access specifier - public
7) constructor       - def __init__(self)
8) Destructor        - we don't have it since we have a Garbage Collector
9) always the first letter of the class name should be capital                              


Ex1:-
-----
# demo for u r class & MRO / datamember / methods
class Person:
   pass


ob1 = Person()                 # creating instance of the CLASS
print(type(ob1))               # <class 'Person'>
print("MRO = ",Person.__mro__) # (<class 'Person'>, <class 'object'>)
print(vars(ob1))               # display object like a dict
print(dir(Person))             # display data mem & methods


Ex2:-
-----
#define methods within the class
#how to invoke the methods via OBJECTS

class Person:
   def greet(self):
      print("HEllo world")

   def show(self):
      print("Hey i am here")


ob1 = Person()                 # creating instance of the CLASS
print(type(ob1))               # <class 'Person'>
print("MRO = ",Person.__mro__) # (<class 'Person'>, <class 'object'>)
print(vars(ob1))               # display object like a dict
print(dir(Person))             # display data mem & methods

ob1.greet()                    # message passing
ob1.show()                     # message passing


Ex3:-
------
# Define a CONSTRUCTOR & methods
# call the methods

class Person:
   def __init__(self):    ## is a constructor
      print("Hey i am BORN....") 

   def greet(self):
      print("HEllo world")

   def show(self):
      print("Hey i am here")


ob1 = Person()   


===============================================================================
Example with fill & other fns:-
-------------------------------

class Player:
 pass


class Person:
   def __init__(self):
      print("I am born")

#          4048 john 10 mum
   def fill(self,name1,age1,city1): 
      # name,age,city are local variables
      # once the method exists values are LOST
      # we have to store these values as DATA MEMBERS
      self.name = name1
      self.age  = age1
      self.city = city1

   def convert(self):
      self.name = self.name.upper()
 
   def show(self):
      print(self.name,self.age,self.city)


#classname.methodname(objectaddress, if_any_arguments)

p1 = Person()  # allocate memory & Then call the CTOR
#Person.__init__(1234)

p2 = Person()  # allocate memort & Then call the CTOR
#Person.__init__(4048)

p1.fill("hari",20, "blr")  # calling the methods
#Person.fill(1234,"hari",20, "blr")

p2.fill("john",10, "mum")  # calling the methods
#Person.fill(4048,"john",10, "mum")

p1.convert()                
#Person.convert(1234)

p1.show()
#Person.show(1234)

p2.show()
#Person.show(4048)


========================================================================
Task:-
=======

class Point:
  def __init__(self):
     pass
  def set_x_value(self, v1):
     self.x = v1
  def set_y_value(self, v2):
     self.y = v2
  def fill(self,v1,v2):
     self.x = v1
     self.y = v2
  def show(self):
     print(" x = %s and y = %s "%(self.x, self.y))
  def incr(self):
     self.x = self.x + 1
     self.y = self.y + 1
  

Given:-
=======
#classname.methodname(objectaddress, if_any_arguments)
# assume p1 address is 8440
# assume p2 address is 6404

p1 = Point()        # Point.__init__(8440)
p1.set_x_value(10)  # Point.set_x_value(8440,10)
p1.set_y_value(20)  # Point.set_y_value(8440,20)
p1.show()           # Point.show(8440)
p1.incr()           # Point.incr(8440)
p1.show()           # Point.show(8440)

p2 = Point()        #
p2.fill(30,40)      #
p2.show()           # X  = 30  and y  = 40

===========================================================================
Ex3:-
------
# Define a CONSTRUCTOR & methods
# call the methods
# COMBINE CTOR & FILL METHOD

class Person:
   def __init__(self,name1,age1,city1):   # ctor & fill is merged
      self.name = name1
      self.age  = age1
      self.city = city1

   def convert(self):
      self.name = self.name.upper()
 
   def show(self):
      print(self.name,self.age,self.city)


p1 = Person("hari", 20, "blr")
p1.convert()
p1.show()

print(vars(p1))  # {"name" : "hari", "age" : 20, "city" : "blr"}

for elem in dir(p1):
   if not str(elem).startswith("_"):
      print(elem)
# age
# city
# convert
# name
# show

OR

print(vars(p1))
datamem = list(vars(p1).keys())
methods = []

for elem in dir(p1):
   if not elem.startswith("_"):
      methods.append(elem)

methods = set(methods) - set(datamem)

print(methods)


-----------------------------------------------------------------------------

Note:
it is a good practice to initialize all the data members
within the CONSTRUCTOR i.e def __init__(self)


Task:-
-------
#Given:-
# Write a class for the following main program

st1 = Student("ravi","cse",[10,20,30,40])
st2 = Student("hari","civ",[40,50,60,70])

st1.findtotal()  # 
st2.findtotal()  #

st1.show()  # name   = ravi
            # stream = cse
            # marks  = [10,20,30,40]
            # total  = 100

solution:-
----------
class Student:
       def __init__(self,name,branch,marks):
              self.name=name
              self.branch=branch
              self.marks=marks
              self.total=0     # good practice

       def findtotal(self):
              self.total = sum(self.marks) # calculated

        def show(self):
               print(self.name,self.branch,self.marks,self.total)
               
      
st1 = Student("ravi","cse",[10,20,30,40])
st2 = Student("hari","civ",[40,50,60,70])
st1.findtotal()  # 


-----------------------------------------------------------------------------------
Major Points w.r.t to classes:-
================================
1) write a class          :  class Person:
2) create an object       :  p1 = Person("hari",20,"blr")
3) access data mem        :  self.name/self.age/self.city
4) invoke methods         :  self.methodname()
5) this pointer           :  "self"
6) Constructor            :  def __init__(self)
7) Destructor             :  not there since we have GC
8) private data member    :  data member name starts with double 
                             underscore - i.e self.__name
9) private method         :  def __methodname(self):
10)class data member      :  common to all the OBJECTS
                             CLASS LEVEL PROPERTY
11)class methods          :  Designed to operate on class data mem
                             @classmethod

12)operator overloading   :  designated methods
                             def __add__(self,other)
                             magic methods

13)inheritance            :  class Derived(Base1,Base2)
                             ctor cascading Base.__init__(self)

14)method over-riding     :
15)slots                  :
16)property               :
17)abstract classes       :



example for private members in python:-
=======================================
class Person:
   def __init__(self,name1,age1,city1):   # ctor & fill is merged
      self.__name = name1
      self.age  = age1
      self.city = city1

   def convert(self):
      self.__name = self.__name.upper()
 
   def show(self):
      print(self.__name,self.age,self.city)


p1 = Person("hari",20,"blr")

print("U R age  = ",p1.age)  #
print("U R city = ",p1.city) #
print("U R name = ",p1.__name) # 


staticmethod - there is no default args
             - can be called via classname (GOOD PRACTICE) 
             - @staticmethod 

classmethod  - default arg is classname
             - can be called via object    (GOOD PRACTICE)
             - @classmethod

example for class data member & class methods:-
===============================================
class Product:
   total = 0   # class data member  

   def __init__(self,name,ctgry,qty):
       self.name  = name
       self.ctgry = ctgry
       self.qty   = qty
       Product.total += self.qty  # adding within ctor

   def foo(self):
       pass  # NULL BODY FUNCTION / STUBS

   def show(self):    
       print(self.name,self.ctgry,self.qty)

   @classmethod
   def display(cls):
       print("CLS   = ",cls)
       print("Total = ",cls.total)


# what is the default arg for the METHODs   - object address
# What is the default arg for CLASS METHODS - CLASSNAME  

# how do we call a method        - object.methodname()
# how do we call a class method  - object.classmethodname()
#                                   classname.classmethodname()
Product.display()
p1 = Product("DVD","hw", 10)
p2 = Product("win","sw", 20)
p3 = Product("HDD","hw", 30)
p4 = Product("anti","sw",40)
p4.display()



Task:-
------

e1 = Emp("ravi",15000)
e2 = Emp("hari",25000)
e3 = Emp("raja",40000)
e4 = Emp("arun",20000)

e1.displayAvgSalary()  # avg salary = ?  

e5 = Emp("yash",35000)

e1.displayAvgSalary()  # avg salary = ?  


solution:-
----------
class Emp():
    total = 0     # Class data members
    count = 0     # class data members

    def __init__(self, name, salary):
        self.name = name
        self.sal  = salary
        Emp.count += 1        # incre the class data member
        Emp.total += self.sal # adding the class data member

    @classmethod
    def displayAvgSalary(cls):
        print("AVG = ",cls.total/cls.count) # Display

    def show(self):
        print(self.name,self.sal)



Operator Overloading:-
======================
a=10
b=20
res = a + b   # math addition 


msg="hello world"
dest="localhost"
final= mesg+dest   # concatenation

a = [10,20,30]
b = [40,50,60]
res = a + b        # merge two lists


Plus operator reacts in different ways
if operand1 & operand2 are integers - addition
                       are strings  - concatenate
                       are lists    - merge


Ex1:-
-----

class Point:
  def __init__(self,x=0,y=0):  # default-cum-paramterized
     self.x = x
     self.y = y

  def show(self):
     print("X = %s and Y = %s" %(self.x,self.y))


p1 = Point(10,20)
p2 = Point(3)

print(p1)   # 
print(p2)   # 


Ex2:-
-----
class Point:
  def __init__(self,x=0,y=0):  # default-cum-paramterized
     self.x = x
     self.y = y

  def show(self):
     print("X = %s and Y = %s" %(self.x,self.y))

  def __str__(self): # toString equivalent of JAVA
     return "X = %s and Y = %s" %(self.x,self.y)


p1 = Point(10,20)
p2 = Point(3)

print(p1)   # 
print(p2)   # 


Operator are already mapped with special functions:-
----------------------------------------------------
  a+b   ==>  a.__add__(b)
  a-b   ==>  a.__sub__(b)
  a*b   ==>  a.__mul__(b)
  a/b   ==>  a.__div__(b)

  a==b  ==>  a.__eq__(b)
  a!=b  ==>  a.__ne__(b)
  a>b   ==>  a.__gt__(b) 
  a>=b  ==>  a.__ge__(b)
  a<b   ==>  a.__lt__(b)
  a<=b  ==>  a.__le__(b)



Ex3:-
-----
class Point:
  def __init__(self,x=0,y=0):  # default-cum-paramterized
     self.x = x
     self.y = y

  def show(self):
     print("X = %s and Y = %s" %(self.x,self.y))

  def __add__(self, other):
     temp = Point()   # always create a temp object
     temp.x = self.x + other.x
     temp.y = self.y + other.y
     return temp



p1 = Point(10,20)
p2 = Point(3)
p3 = p1 + p2  # p3 = p1.__add__(p2)
              # p3 = Point.__add__(p1,p2)
p3.show()


Task:-
------

Given:-
--------

arr1 = Array([10,20,30,40])
arr2 = Array(["a","b","c","d"])

if arr1 == arr2:
   print("Equal")
else:
   print("UnEqual")


arr3 = arr1 + arr2

print(arr3)   # [10, "a", "20, "b", "30, "c", "40", "d"]


solution:-
----------
class Array:
  def __init__(self,lst):
     self.lst = lst

  def __str__(self):
     return self.lst

  def __eq__(self,other):
     self.lst == other.lst

  def __add__(self,other):
     return list(zip(self.lst,other.lst))


arr1 = Array([10,20,30,40])
arr2 = Array(["a","b","c","d"])

if arr1 == arr2:
   print("Equal")
else:
   print("UnEqual")


arr3 = arr1 + arr2

print(arr3)   # [10, "a", "20, "b", "30, "c", "40", "d"]



Example for Inheritance:-
=========================

Single level inheritance
multi level inheritance
multiple inheritance
hierarchical inherit
hybrid inheritance


>> Specialization
>> IS-A relationship


Ex1:-
-----
class Base:
  def __init__(self,name,desig):
      self.name = name
      self.desig = desig

  def show(self):
      print("BASE = ",self.name,self.desig)


class Derived(Base):             # Inherit a class in python
  def __init__(self,name,desig,loc,sal):
      Base.__init__(self,name,desig)   # CTOR cascading
      self.loc = loc
      self.sal= sal

  def display(self):
      print("Derived = ",self.loc,self.sal)


ob1 = Derived("hari", "SSE", "blr", 56000)
print(vars(ob1)) # {name = ?
                 #   desig = ?
                 #   loc   = ?
                 #   salary = ? }
ob1.show()   # 
ob1.display()


Note:
  -class Derived(Base1,Base2)  # possible
  -Base1.__init__(self,a) 
  -Base2.__init__(self.b)
  -Derived class will be able to access methods of base classes


Task:-
-------

solution for the task:-
-----------------------
class Bowler:
  def __init__(self,name,team):
     self.name = name
     self.team = team
  def show(self):
     print(self.name,self.team)

class Spinner(Bowler):
  def __init__(self,name,team,type):
     Bowler.__init__(self,name,team)      
     self.type = type
  def sp_show(self):
     print(self.type)

class Fast(Bowler):
  def __init__(self,name,team,pace,speed):
     Bowler.__init__(self,name,team)      
     self.pace = pace
     self.speed= speed
  def fast_show(self):
     print(self.pace,self.speed)


ob1 = Spinner("kumble","india","leg")
ob2 = Fast("Bomrah","india", "fast",150)
ob1.show()
ob1.sp_show()          
ob2.show()   
ob2.fast_show()


------------------------------------------------------------------------------
Example for MEthod over-riding:-
================================
Ex1:-
=====
class Alpha:
   def fun1(self):
      print("Alpha-Fun1")

class Beta:
   def fun2(self):
      print("Beta-Fun2")

class Delta(Alpha,Beta):
   def fun3(self):
      print("Delta-Fun3")

class Omega(Delta):
   def fun4(self):
      print("Omega-Fun4")


ob = Omega()
ob.fun1()     # Method Resoultion Order (MRO)
#print("\n".join(str(e) for e in Omega.__mro__))
# Bottom up Left to Right




Ex2:-
=====
class Alpha:
   def fun1(self):
      print("Alpha-Fun1")

class Beta:
   def fun1(self):
      print("Beta-Fun1")

class Delta(Alpha,Beta):
   def fun1(self):
      print("Delta-Fun1")

class Omega(Delta):
   def fun4(self):
      print("Omega-Fun4")

# How many version of fun1 are there - 3
# alpha version
# beta version
# delta version

ob = Omega()
ob.fun1()    # pick the Delta version   



Ex3:-
=====
class Alpha:
   def fun1(self):
      print("Alpha-Fun1")

class Beta:
   def fun1(self):
      print("Beta-Fun1")

class Delta(Alpha,Beta):
   def fun3(self):
      print("Delta-Fun3")

class Omega(Delta):
   def fun4(self):
      print("Omega-Fun4")

# How many version of fun1 are there - 2
# alpha version
# beta version

ob = Omega()
ob.fun1()    # pick the Alpha version


Ex4:-
-----
class Alpha:
   def fun1(self):
      print("Alpha-Fun1")

class Beta:
   def fun1(self):
      print("Beta-Fun1")

class Delta(Alpha,Beta):
   def fun1(self):          # should call Alpha fun1 & Beta fun1
      super().fun1()        # super also follows MRO
      Beta.fun1(self)       # avoid this as far as possible
      print("Delta-Fun1")

class Omega(Delta):
   def fun4(self):
      print("Omega-Fun4")


# derived version should call the all the versions of the 
# BASE classes

ob = Omega()
ob.fun1()    # pick the Delta version



Task:-
======
class Decimal:
  def __init__(self,num):
      self.num = num
  def show(self):
      print("Decimal = ",self.num)

class Binary(Decimal):
  def __init__(self,num):
      Decimal.__init__(self,num) # this initialize num
  def show(self):
      super().show()
      print("Binary = ",bin(self.num))

class Hexa(Decimal):
  def __init__(self,num):
      Decimal.__init__(self,num) # this initialize num
  def show(self):
      super().show()
      print("Hexa = ",hex(self.num))

ob1 = Binary(21)
ob1.show()
ob2 = Hexa(15)
ob2.show()


================================================================================
slots in python:-
=================
>> Objects in python are stored as Dictionary
>> size of the dict is DYNAMIC
>> they will occupy more memory

Ex1:-
------
class Person: 
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc
   

p1 = Person("arun",20, "blr")

print(vars(p1))


Ex2:-
-----
class Person: 
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc
   def show(self):
      print("Name = ",self.name)
      print("Age  = ",self.age)
      print("Loc  = ",self.loc)
   

p1 = Person("arun",20, "blr")
print(vars(p1))

p1.email = "arun@india.com"  # add a new data member - "email"
print(vars(p1))

Note:
 in the above program p1.email="arun@india.com" statement
 is an assignment statement - it will automatically create
 a new key "email" with value as "arun@india.com"
 since object is a DICTIONARY


Ex3:-
=====
# data members are FIXED 
# once we enable slots object aren't dictionaries
# FIXED - add / delete new data members
# print(vars(object))  will throw an ERROR

class Person: 
   __slots__ = ["name", "age", "loc"] # fixed data members

   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def show(self):
      print("Name = ",self.name)
      print("Age  = ",self.age)
      print("Loc  = ",self.loc)
   

p1 = Person("arun",20, "blr")
p1.show()
#print(vars(p1))

p1.email = "arun@india.com"  # add a new data member - "email"
#print(vars(p1))


------------------------------------------------------------------------------
property:-
==========
Ex1:-
=====
class Person: 
   def __init__(self,name):
      self.setname(name)

   def show(self):
      print("Name = ",self._name)

   def setname(self,name):
      if name.isalpha():
         self._name = name
      else:
         self._name = "EMPTY"

   def getname(self):
      return "HEY HOW ARE U "+self._name

   name = property(getname, setname)


p1 = Person("john")
print("U r name = ",p1.getname())
p1.name = "12345"
print("U R Name = ",p1.getname())
      

Ex2:-
=====
>> property with slots 

class Person: 
   __slots__ =[ "__name"]
   def __init__(self,name):
      self.setname(name)

   def show(self):
      print("Name = ",self.name)

   def setname(self,name):
      if name.isalpha():
         self.__name = name
      else:
         self.__name = "EMPTY"

   def getname(self):
      return "HEY HOW ARE U "+self.__name

   name = property(getname, setname)

p1 = Person("john")
print("U R NAme = ",p1.name)
p1.__name = "123435"
print("U R NAme = ",p1.name)



=================================================================================
Abstract class:-
================
>> abc - Abstract Base Classes
>> partially know functions & partially unknown functions
>> any class which has atleast one abstract function such classes
   are called as abstract base classes
>> Such class cannot be instantiated
>> can be derived
>> derived it compulsory to re-define the abstract methods

Ex1:-
=====
from abc import *   

class Person(metaclass=ABCMeta):
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def show(self):
      print(self.name,self.age,self.loc)

   @abstractmethod
   def setband(self):
      pass


p1 = Person("arun",20,"blr")
p1.show()

ERROR :
--------
Traceback (most recent call last):
  File "prog1.py", line 17, in <module>
    p1 = Person("arun",20,"blr")
TypeError: Can't instantiate abstract class Person with abstract methods setband


Ex2:-
=====
from abc import *   

class Person(metaclass=ABCMeta):
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def show(self):
      print(self.name,self.age,self.loc)

   @abstractmethod
   def setband(self):
      pass

class NewPerson(Person):
   def __init__(self,name,age,loc,salary):
       super().__init__(name,age,loc)
       self.salary = salary
       self.band = None
   def show(self):
       super().show()
       print("BAND = ",self.band)


p1 = NewPerson("arun",20,"blr",45000)
p1.show()

ERROR MESSAGE:-
---------------
Traceback (most recent call last):
  File "prog1.py", line 31, in <module>
    p1 = NewPerson("arun",20,"blr",45000)
TypeError: Can't instantiate abstract class NewPerson with abstract methods setband
      

EX3:-
======
>> Final program

from abc import *   

class Person(metaclass=ABCMeta):
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def show(self):
      print(self.name,self.age,self.loc)

   @abstractmethod
   def setband(self):
      pass

class NewPerson(Person):
   def __init__(self,name,age,loc,salary):
       super().__init__(name,age,loc)
       self.salary = salary
       self.band = None
   def setband(self):
       if self.salary >=25000:
          self.band = "BAND1"
       else:
          self.band = "BAND2"
   def show(self):
       super().show()
       print("BAND = ",self.band)


p1 = NewPerson("arun",20,"blr",45000)
p1.setband()
p1.show()

=====================================================================================     
class MouseEvents:

   @abstractmetod
   def rightclick(self):
       pass

   @abstractmetod
   def leftclick(Self):
       pass  


class BankingApp(MouseEvents):
    



if somebody right clicks what shld be done
will be known by that somebody or ME

========================================================================= 
Life cycle of an object:-
=========================

BORN----> def __new__() ---->  def __init__(self)---->?--->def __del__()

>> defining def __new__ - very rare cases


class Person:
  def __new__(cls,*args,**kwargs):
     print("NEW called")
     return super().__new__(*args,**kwargs)
  
  def __init__(self):
     print("INIT called")

  def __del__(self):  # only CLI executions not GUI Executions
     print("DEL called")

p1 = Person()


===========================================================================
unbound calls of python:- 
=========================
>> avoid these types of calls in a class

>>bound methods   - default args - OBJECTS address
>>unbound methods 
>>static methods  - default args - NOTHING
>>class methods   - default args - CLASSNAME

BOUND METHODS are BOUND TO AN OBJECT

how can we call a BOUND METHOD  - via OBJECT
how can we call a STATIC METHOD - via CLASSNAME
how can we call a CLASS METHOD  - via OBJECT

ex:-
----
>>> class Sample:
...   def fun1(self):
...     pass
...   @staticmethod
...   def fun2():
...     pass
...   @classmethod
...   def fun3(cls):
...     pass
...
>>> ob = Sample()
>>> ob.fun1
<bound method Sample.fun1 of <__main__.Sample object at 0x00000167FDC10358>>
>>> ob.fun2
<function Sample.fun2 at 0x00000167FDBF4730>
>>> ob.fun3
<bound method Sample.fun3 of <class '__main__.Sample'>>
>>>

are staticmethod - BOUND METHOD - NO
are classmethods - BOUND METHOD - YES

WHAT IS an UNBOUND METHODs?
-----------------------------
>> according to python we can call ANY METHOD in a UNBOUND WAY
   CLASSNAME.METHODNAME(objectaddres,if_any_args)
>> aren't bound to any OBJECT
>> are UN-CONVENTIONAL
>> avoid calling any METHOD in UNBOUND WAY
>> typically  unbound way is used
   1) constructor cascading
   2) multiple base classes - Multiple inheritance


================================================================================
Monkey Patching :-
==================
>> Since python functions/methods are LOOSELY binded with 
   function-names 

>> Applications 
   unittesting  - mock
   asynchronous - execution

ex:-
----
class Person:
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def show(self):
      print(self.name,self.age,self.loc)


p1 = Person("hari", 25, "blr")
p1.show()
oldaddress = Person.show
def myown(x):
   print(x.name.upper(), x.age, x.loc.upper())
Person.show=myown  # replacing the OLD address with myown address

p1.show()   # new behaviour

Person.show = oldaddress
p1.show()   # old behaviour


program -  generic

windows -  monkey patching
unix    -  monkey patching
linux   - monkey patching
mac     - monkey patching

===================================================================================
Iterator:-
===========
>> Iterable is a collection i.e str/tuple/list/set/dict/file
>> Iterator is a pointer which moves on the collection
>> Iterator is POINTER in a disguise
>> Iterator moves from FIRST element 
>> stops when it encounter an exception - StopIteration

arr = [10,20,30,40,50]  # collection  or Iterable

for cursor in arr:      # cursor      or Iterator
    print(cursor)

Ex1:-
-----
class Person:
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def show(self):
      print(self.name,self.age,self.loc)

p1 = Person("yash", 25, "blr")

for cursor in p1:   
  print(cursor)


Error output:-
--------------
Traceback (most recent call last):
  File "prog1.py", line 12, in <module>
    for cursor in p1:
TypeError: 'Person' object is not iterable


Ex2:-
======
>> According to python any class can be ITERABLE
   by over-riding two special methods
   1) def __iter__(self)
   2) def __next__(self)

class Person:
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def show(self):
      print(self.name,self.age,self.loc)

   def __iter__(self):
      return iter([self,self.name,self.age,self.loc])

   def __next__(self):
      pass
p1 = Person("yash", 25, "blr")

for cursor in p1:   
  print(cursor)



Ex3:-
=====
>> According to python any class can be ITERABLE
   by over-riding two special methods
   1) def __iter__(self)
   2) def __next__(self)

class Person:
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc
      self.count = 0

   def show(self):
      print(self.name,self.age,self.loc)

   def __iter__(self):
      return self

   def __next__(self):
      self.count = self.count+1
      if self.count == 1:
         return self.name
      elif self.count == 2:
         return self.age
      elif self.count == 3:
         return self.loc
      else:
         self.count=0
         raise StopIteration()

p1 = Person("yash", 25, "blr")

for cursor in p1:   
  print(cursor)

print("once again looped")
for cursor in p1:   
  print(cursor)


================================================================================

150 def add(a,b):
151    a=a+5
152    b=b+2
153    res=a+b
154    return res
155
156 p=10
157 q=20
158 ans = add(p,q) ===> converted ans=goto 150 & comeback
159 print("RESULT = ",ans)


Internally within the micro-processor we have a special
register which holds the address of the CURRENT INSTRUCTION
PC - program counter

Generator:-
============
>> any function/method has a keyword "yield"
   such functions are termed as generator functions
>> when we call a generator function it returns the CODE ADDRESS
>> execution starts only when we iterate
>> a function can return keyword too - at the LAST
                                     - NULL return
>> return exits the function
>> yield  returns the values & Still preserve the state of FUNCTION
          until the last yield statement

Ex:-
=====
#150 def callme():
#151    a=10
#152    yield a+5
#153    b=10
#154    c=30
#155    yield a+b+c
#156    d=5
#157    yield b+c+d
#158    yield a+b+c+d

def callme():
   a=10
   yield a+5
   b=10
   c=30
   yield a+b+c
   d=5
   yield b+c+d
   yield a+b+c+d


it = callme() # it returns the code address - 150
print(it) # Where is the PC=150
res=next(it)  # now execution starts & stops at yield & Return value
print("RESULT = ",res) # now the control IS IN MAIN PROGRAM
                       # our FUNCTION IS IN IDLE STATE
res=next(it) # new exeu start & Stops at yield & Return values
print("RESULT = ",res)


OR

for elem in callme():
   print("RESULT  = ",elem)


Major differnce b/w Iterator and Generator :-
---------------------------------------------
Iterator  - iterates on DATA
Generator - iterates on CODE

Applications:-
==============
>> Lazy execution model
>> Batch processing 
>> Asynchronus executions


problem:-
==========
Server RAM size = 20 GB
Swap Space      = 40 GB
MAX PROGRAM SIZE allowed = 60GB

Now we have a DATA FILE Which is 1TB how will we load them

we will have to load BLOCK BY BLOCK as & When needed
in python we use GENERATOR for such problems

best example for generator:-
----------------------------
range(start,stop,step)

>>>
>>> range(1,11,1).__sizeof__()
48
>>> range(1,101,1).__sizeof__()
48
>>> range(1,1001,1).__sizeof__()
48
>>> range(1,10001,1).__sizeof__()
48
>>> range(1,100001,1).__sizeof__()
48
>>>

================================================================================
co-routines:-
==============
 https://stackabuse.com/coroutines-in-python/

Generators produce data

Coroutines consume data


What are callbacks ?
=====================
>> a function reference is passed as a argument
   to another function
>> function can call this functionref at any point

ex:-
-----

def callback(fnref):
  print("I AM CALL BACK FUNCTION")
  print("FN ref = ",fnref)
  fnref()

def square():
  print("HEllo square")

def cube():
  print("Hell cube")


callback(square)
callback(cube)



design a object as callbacks:-
===============================
Ex1:-
-----
class Person:
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

 
p1 = Person("harish", 20, "blr")
p1()

ERROR OUTPUT:-
--------------
Traceback (most recent call last):
  File "prog1.py", line 10, in <module>
    p1()
TypeError: 'Person' object is not callable

Ex2:-
------

class Person:
   def __init__(self,name,age,loc):
      self.name = name
      self.age  = age
      self.loc  = loc

   def __call__(self):
      print("Hello world")
      

 
p1 = Person("harish", 20, "blr")
p1()

Output:-
---------
Hello world

===================================================================================
Function Wrappers:-
-------------------
>> callbacks
>> when we have to add extra functionality to the existing functions
   without modifying the actual functions
>> we have OLD VERSION  - directly
   we have NEW VERSION  - via wrapper
>> did we change calling convention - YES

#filename = mathlib.py:-
#-----------------------
def wrapper(fnref,*args,**kwargs):
  print("Extra functionality")  
  res = fnref(*args,**kwargs)
  return res

def square(num):
  res = num*num
  print("SQuare = ",res)

def add(a,b):
  res = a + b
  print("ADD = ",res)

def express(a,b,c):
  ans = a + b**2 /c
  print("EXP = ",ans)

def greet():
  print("Good morning....")

#filename = another.py:-
#------------
import mathlib

mathlib.wrapper(mathlib.square, 5)     # extra functionality
mathlib.wrapper(mathlib.add,10,20)     # extra functionality
mathlib.wrapper(mathlib.express,5,6,7) # extra functionality
mathlib.wrapper(mathlib.greet)         # extra functionality

mathlib.square(5)         # normal call



Nested Functions:-
==================
>> defining a function within a function 

def outer(mesg):
   print("Hey i am outer",mesg)
   a=10
   b=20
   def inner():
     c=30
     ans=a+b+c
     print("ANS = ",c)
   inner()

outer("HEllo world")
  


Closures:-
===========
>> 1) NEsted fns
   2) Inner function should be dependent on outer values
   3) return address of inner function

>> Closure hold the address of the OUTER fn values which are
   used in the inner function

def outer(mesg):
   print("Hey i am outer",mesg)
   a=10
   b=20
   def inner():
     c=30
     ans=a+b+c
     print("ANS = ",c)
   return inner

# Can we call inner function - outside the "outer" function
#   (yes by returning the address)

fnref = outer("hello world")
print(fnref)
print("NAME = ",fnref.__name__) 
print("DEF  = ",fnref.__defaults__)
print("CODE = ",fnref.__code__)
print("CLOSURE = ",fnref.__closure__)

NOte:
if fnref.__closure__ is None - then it is not a CLOSURE
if fnref.__closure__ is NOT None - then it is CLOSURE


Decorator:-
===========
#filename = mathlib.py:-
#-----------------------

def outer(fnref):
  def wrapper(*args,**kwargs):
     print("Extra functionality-BEFORE")  
     res = fnref(*args,**kwargs)
     print("Extra functionality-AFTER")  
     return res
  return wrapper

@outer            # square = outer(square)
def square(num):
  res = num*num
  print("SQuare = ",res)

@outer
def add(a,b):
  res = a + b
  print("ADD = ",res)

@outer
def express(a,b,c):
  ans = a + b**2 /c
  print("EXP = ",ans)

@outer
def greet():
  print("Good morning....")

#filename : another.py
#---------------------
import mathlib

mathlib.greet()


Applications :-
---------------
>> loggers
>> @classmethod
>> @staticmethod
>> @abstractmethod
>> timeit

==================================================================================


>>> class Point:
...   def __init__(self,x,y):
...      self.x = x
...      self.y = y
...   def show(self):
...      print(self.x,self.y)
...
>>> p = Point(10,20)
>>> hasattr(p, "x")
True
>>> hasattr(p, "y")
True
>>> hasattr(p, "z")
False
>>> hasattr(p, "show")
True
>>>

==================================================================================
Design Patterns:-
=================
   decorator
   iterator
   singleton pattern - a class can have only one object
   factory method    - can produce diff type of objects
   abstract factory  - collection of factory


Example for SINGLETON/BORG Pattern:-
======================================
class Singleton:

  def __new__(cls, *args, **kwargs):
    if not hasattr(cls, "_inst"):
      #cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
      cls._inst = super().__new__(cls, *args, **kwargs)
    return cls._inst
  
  def fun(self):
    print("Fun...")


s = Singleton()
s.fun()

s1 = Singleton()
s1.fun()
print(id(s))
print(id(s1))


Example for singleton pattern:-
--------------------------------
loggers
stdin
stdout
stderr


Example for Factory method:-
----------------------------

I have differnt type of songs
 Devosongs
 InstSongs
 JazzSongs
 RockSongs

I have a PlayList
  addsongs to the playlist
  play all the songs
  total duration of all songs


solution:-
----------
from abc import *

class Songs(metaclass=ABCMeta):
   def __init__(self,name,duration):
      self.name=name
      self.dur =duration
   @abstractmethod
   def play(self):
      pass

class Devo(Songs):
   def __init__(self,name,duration):
      super().__init__(name,duration)
   def play(self):
      print("Devo song played")

class Inst(Songs):
   def __init__(self,name,duration):
      super().__init__(name,duration)
   def play(self):
      print("Inst song played")

class Jaaz(Songs):
   def __init__(self,name,duration):
      super().__init__(name,duration)
   def play(self):
      print("Jaaz song played")
      
class Rock(Songs):
   def __init__(self,name,duration):
      super().__init__(name,duration)
   def play(self):
      print("Rock song played")

class SongsFactory:
   def __init__(self):
      pass
   def getSong(self,num,name,dur):
      if num==1:
         return Devo(name,dur)
      elif num==2:
         return Inst(name,dur)
      elif num==3:
         return Jaaz(name,dur)
      else:
         return Rock(name,dur)


plst = []
sf = SongsFactory()
plst.append(sf.getSong(4,"SONG-4", 10))
plst.append(sf.getSong(1,"SONG-1", 10))
plst.append(sf.getSong(2,"SONG-2", 10))
plst.append(sf.getSong(3,"SONG-3", 10))
print(plst)
total=0
for elem in plst:
   elem.play()
   total+=elem.dur

print("Total duration = ",total)



Abstract FActory:-
==================

class WheelFactory:
class ChassisFactory:
class BodyFactory:
class EngineFactory
class SparesFActory


class AbsractBus:
    def __init__(self):
       ob1 = WheelFactory()
       ob2 = ChassisFactory()
       ob3 = BodyFactory()
       ob4 = EngineFactory()
       ob5 = SparesFActory()

>> Iterator
>> Decorators


==============================================================================
Functional programming:-
=========================
>> we will never use for-iterator or if-else


1) lambda expressions  - one liner functions
                       - un-named functions

2) map algorithm      - it = map(fnref/lambda , iterable)

3) filter algorithm   - it = filter(fnref/lambda , iterable)
                        ( lambda will return a boolean value )

4) reduce algorithm   - see later

5) partial functions  - see later

6) import functools   - see later

7) import itertools   -


example for lambda expressions:-
--------------------------------
f(x) = x + 5

function name = "f"
how many args =  1
arg name      =  "x"
type arg      =  int

def f(x):
  return x + 5
OR
f = lambda x : x + 5

f(10) =  15
f(6)  =  11



f1(10,20)               =>  30
f2([30,10,40,20,50])    => 2nd max
f3("ravi kumar sharma") => sharma
f4("10,20,30,40,50")    => sum
f5(10,30)               => return max

solution:-
----------
f1 = lambda x,y : x + y
f2 = lambda x   : sorted(x)[-2]
f3 = lambda x   : x.split()[-1]
f4 = lambda x   : sum(int(e) for e in x.split(","))
f5 = lambda x,y : x if x>y else y

Applications:-
---------------
 >> custom sorts
 >> callbacks
 >> functional programming


example for map:-
=================
numlst = [1,2,3,4,5,6,7]
res = list(map(lambda x: x*x,  numlst))
print(res) # [1,4,9,16,25,36,49]


example for filter:-
====================
numlst = [ 11,3,6,8,43,50,23,10 ]

res = list(map(lambda x : x%2==0 , numlst))
print(res)

res = list(filter(lambda x : x%2==0 , numlst))
print(res)


Task:-
-------
datalst = ["blr=20", "chn=10", "mum=30", "hyd=40", "tvm=15"]


res1 = ["blr", "chn", "mum", "hyd", "tvm"]
res2 = ["mum=30", "hyd=40"]

res1 = list(map(lambda x :x.split("=")[0], datalst))
res2 = list(filter(lambdax x:int(x.split("=")[1])>=40, datalst)

print(res1)
print(res2)


example for iterools:-
=======================

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

pair of 2 which sum 8
pair of should be distinct

(1,7)
(5,3)
(6,2)

import itertools

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

res = itertools.combinations(arr,2)
      #[(1,2),(1,3),(1,4),(1,5)......   ]

ans = filter(lambda x : sum(x)==8, itertools.combinations(arr,2))

print(list(ans))




Comprehnsion:-
==============

alst = [e*e for e in arr]  # list comp

res = {e*e for e in arr }  # set compre

res = {key:value for key,value in zip(alst,blst) } # dict compre

res = (e*e for e in arr )  # generator comp


ex:-
=====
import time


start = time.time()
res = list(map(lambda x : x*x, range(1,1000001)))
end = time.time()


print("MAP = ",end-start)

start = time.time()
res = [x*x for x in range(1,1000001)]
end = time.time()

print("COMP = ",end-start)


====================================================================================
Person = CPU
JOB    = TASK


one person - one job   = uni processing / uni Tasking
one person - many jobs = multi tasking

many person - many jobs = multi processing
many person - same job  = multi processing  

multitasking    - Threads
multiprocessing - Process


import threading       - Thread
import multiprocessing - Process
import subprocess
import concurrent


import threading
import time
import os

def job1():
   print("Hello job1",os.getpid())
   time.sleep(5)

def job2():
   print("Hello job2",os.getpid())
   time.sleep(3)

if __name__ == "__main__" : 
   print("Main Program = ",os.getpid())
   t1 = threading.Thread(target = job1, args=())
   t2 = threading.Thread(target = job2, args=())

   start = time.time()
   t1.start()
   t2.start()

   t1.join()  # process has to wait until threads are completed  
   t2.join()  # process has to wait until threads are completed  

   end = time.time()
   print("Took = ",end-start)
