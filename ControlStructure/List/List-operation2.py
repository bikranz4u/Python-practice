#To check if an item is in a list, the "in" operator can be used. 
#It returns True if the item occurs one or more times in the list, and False if it doesn't.

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
print("===================================")
#The "in" operator is also used to determine whether or not a string is a substring of another string.

name="Tester"
print("Test" in name)  #True
print("eser" in name)  #False


print("===================================")
#What is the result of this code?
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5   # 9-5 = 4
if 4 in nums:
  print(nums[3])    #O/p:- 7
else:
  print(nums[4])

print("===================================")
#To check if an item is not in a list, you can use the not operator in one of the following ways:
nums = [1, 2, 3]
print(not 4 in nums)    #True
print(4 not in nums)    #True
print(not 3 in nums)    #False
print(3 not in nums)    #False

print("===================================")
letters = ['a', 'b', 'z']
if "z" in letters:
    print ("Yes")
