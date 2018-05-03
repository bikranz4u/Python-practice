str=input("Enter you a string to reverse:")
#Resolution ----> Way-1
print('The reversed string using slice (): ',str [::-1])

#Resolution ----> Way-2
print('The reversed string using reversed ():',reversed(str))  #<reversed object at 0x000002989C7252B0>
#reversed refers to the memory location , we need to fetch that
for x in reversed(str):
    print(x)
print(''.join(reversed(str)))

#Resolution ----> Way-3
i = len(str) - 1
desired = ''
while i >= 0:
    desired = desired + str[i]
    i = i - 1
print('The reversed string using \'while\' is:',desired)

#Resolution ----> Way-4
i = len(str) - 1
desired = ''
for i in range(len(str)-1,-1,-1):
    desired = desired + str[i]
print('The reversed string using \'for\' is:',desired)



