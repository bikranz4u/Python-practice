# WAP to merge chars of 2 strings into a single string by taking characters alternatively.
s1=input('Enter the 1st string:')  #Test
s2=input('Enter the 2nd string:')  #Rest
output=' '                         #Expected Output:-TReesstt
i,j = 0,0
#while i < len(s1):
while i < len (s1) or j < len(s2):
    if i < len(s1):
        output= output + s1[i]
        i = i + 1
    if j < len (s2):
        output = output + s2[j]
        j = j + 1
print(output)

#Way-2
