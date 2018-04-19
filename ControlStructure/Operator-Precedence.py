#Operator precedence is a very important concept in programming. 
#It is an extension of the mathematical idea of order of operations 
#(multiplication being performed before addition, etc.)
# to include other operators, such as those in Boolean logic. 

#Python's order of operations is the same as that of normal mathematics: 
#parentheses first -> then exponentiation ->then multiplication/division -> then addition/subtraction.

print ("=================== or operator============")
print (False == False or True)   #True or True => True
print (False == (False or True)) #False == True => False
print ((False == False) or True) #True or True => True
print ("============================================")

print ("=================== and operator============")
print (False == False and True)  #True and True => True
print (False == (False or True)) #False == False => False
print ((False == False) or True) #True or True => True
print ("============================================")

print ("What is the result of this code?")
if 1 + 1 * 3 == 6: 
    print("Yes")
else:
    print("No")