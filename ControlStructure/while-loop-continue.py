#continue

#Another statement that can be used within loops is "continue". 
#Unlike break, continue jumps back to the top of the loop, rather than stopping it.


i = 0
while True:
    i = i + 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)
print("Finished")

#Using the continue statement outside of a loop causes an error.