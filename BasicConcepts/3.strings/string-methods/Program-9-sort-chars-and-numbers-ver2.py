# WAP to sort characters of the string and mupltiply with followed by numeric Values
#I/P:-B4A1D3
#O/P:-BBBBADDD
s=input("Enter a string: ")
output=''
for x in s:
    if x.isalpha():
        output = output + x
        previous = x
        
    else:
        output = output + previous * (int(x) - 1)
    if x.isdigit():
            num= int(x)
    print(num)
    else:
        output = output + x
print(output)