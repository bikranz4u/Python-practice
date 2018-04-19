#To end a while loop prematurely, the break statement can be used. 
#When encountered inside a loop, the break statement causes the loop to finish immediately.
#Using the break statement outside of a loop causes an error.


#How many numbers does this code print?
i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break