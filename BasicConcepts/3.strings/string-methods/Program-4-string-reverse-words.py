str=input("Enter  a string to reverse the words in the string :")
#I/P:- Test Is Good
#O/P:- Good Is Test
lst=str.split()  # You can mention separator here
print(lst)      #['Test', 'Is', 'Good']
output=[]
i = len(lst) - 1
print(i)     # Length of the list
while i >= 0:
    #output = output + lst[i] # desired = desired + str[i]
    output.append(lst[i])
    i = i - 1
print(output)   #['good', 'is', 'test']
print(' '.join(output))



# Way 2

for x in lst:  #range(start,stop,step)
    output.append(lst[i])
    i = i - 1
print(' '.join(output))    