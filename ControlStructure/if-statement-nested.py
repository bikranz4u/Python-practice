#if statements can be nested, one inside the other.
#This means that the inner if statement is the statement part of the outer one. 
#This is one way to see whether multiple conditions are satisfied. 

num = int(input ("Enter a number:"))
if num > 10:
    print ("Num is greater than 10")
    if num < 10:
        print ("Num is lesser than 10")
# Different Types of execution
num = 12
if num > 5:
    print("Bigger than 5")
    if num <=47:
        print("Between 5 and 47")