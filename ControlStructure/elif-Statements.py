#The elif (short for else if) statement is a shortcut to use when chaining if and else statements.
# A series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True.
num = int(input("Enter the number: "))
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")