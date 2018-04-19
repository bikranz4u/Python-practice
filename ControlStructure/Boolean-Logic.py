#Boolean logic is used to make more complicated conditions for if statements that rely on more than one condition. 
#Python's Boolean operators are and, or,  not. 
#The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True. Otherwise, it evaluates to False.
#Python uses words for its Boolean operators, whereas most other languages use symbols such as &&, || and !.
x = 5
y = 5

a = 2
b = 2
print ("################### and boolean operator #######################")

print ( x == y and a == b)  #True and True = True

print ( x >= y and y >= x)  #True and True = True

print ( x == y and y > x)   #True and False = False

print ("################### or boolean operator #########################")

print ( x == y or y > x)    #True or False = True

print ( y > x or x != y)    #False or False =False

print ( a != b or y >= x)   #False or True = True

print ("################### not boolean operator ########################")

#Unlike other operators we've seen so far, not only takes one argument, and inverts it. 
#The result of "not True" is False, and "not False" goes to True.

x = 5
y = 6

not x == y
print ("False")

not x < y
print ("True")