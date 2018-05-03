#WAP to print Character at odd or Even Position in a string
#I/P:- Test
#O/P:- Even Postion --->

str=input("Enter  a string to check  characters position :")
print('Character is at Even Position using split():',str[::2])
print('Character is at Odd Position using split():',str[1::1])



#-------------Way 2
print("Character is at Even Position :")
i=0
while i < len(str):
    print(str[i])
    i=i+2

print("Character is at Odd Position :")
i=1
while i < len(str):
    print(str[i])
    i=i+1
