# The infinite loop is a special kind of while loop; it never stops running. 
# Its condition always remains True. 
while 1==1:
    print("In the loop")
    break   #Forcefully breaaking the loop

#Fill in the blanks to create a loop that increments the value of x by 2 and prints the even values.
x = 0 
while x <=20:
    print (x)
    x += 2

#How many numbers does this code print?
i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break