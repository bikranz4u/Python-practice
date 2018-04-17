#In Python, it's impossible to complete certain operations due to the types involved.
#For instance, you can't add two strings containing the numbers 2 and 3 together to produce the integer 5, 
#as the operation will be performed on strings, making the result '23'.
#The solution to this is type conversion.

print (int("2") + int("3"))  #O/P: 5
print ("2" + "3") #O/P: 23
print (int(a) + int(b))  #O/P:NameError: name 'a' is not defined

