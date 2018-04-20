# "strings", can be indexed like lists
# Indexing strings behaves as though you are indexing a list containing each character in the string. 

str="Test It"
print(str[3])

#Other types, such as integers, indexing them isn't possible, and it causes a TypeError.

#Which line of code will cause an error?
num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
print(num[5])


