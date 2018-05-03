#WAP to reverse the characters in of the Word's in the String
#I/P:- Test Is Good
#O/P:-tseT sI dooG
str=input("Enter  a string to reverse the words characters :")
lst=str.split()
output=[]
for i in range(len(lst)):     #for x in lst:   can also be used
    str1=lst[i]
    output.append(str1[::-1])  #Word Reversed using Split()
print(output)  #['tseT', 'sI', 'dooG']
print(' '.join(output))  #tseT sI dooG
