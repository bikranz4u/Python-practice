#To get the number of items in a list, you can use the len function.
#Unlike "append", "len" is a normal function, rather than a method. 
#This means it is written before the list it is being called on, without a dot.

nums = [1, 3, 5, 2, 4]
print(len(nums))
print("===================================")
nums1 = [1,"Test", 5.0 , 2, 4, 3.2]
print(len(nums1))

print("===================================")
#What is the result of this code?
letters = ["a", "b", "c", 6]
letters.append("d")
print("No Of items in the list is: ",len(letters))  #O/p-4
