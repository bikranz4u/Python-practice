# WAP to sort characters of the string and first aphabet Symbols followed by numeric Values
#I/P:-B4A1D3
#O/P:-BAD413  or ABD134
str1=input("Enter a string: ")
s1=s2=output=' '
for x in str1:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
print(s1)  #It Will Print only Characters
print(s2)  #It will print only numbers
print(''.join(sorted(s1)) + ''.join(sorted(s2)))

# WAY 2 using sorted()
str1=input("Enter a string: ")
s1=s2=output=' '
for x in sorted(str1):
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
print(''.join(s1) + ''.join(s2))
