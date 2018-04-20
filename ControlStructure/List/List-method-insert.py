#The insert method is similar to append, 
#except that it allows you to insert a new item at any position in the list, 
#as opposed to just at the end.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print (words)

print("================================")
nums = [1,2,3,5,6,7]
index = 3
nums.insert(index,4)   # it allows you to insert a new item at any position
print("We have added 4 to the list ", nums)
nums.append(8)
print("We have added 8 (at the end) to the list ", nums) #it allows you to insert a new item only at end of the list.

print("================================")
#What is the result of this code?
nums = [9, 8, 7, 6, 5]
nums.append(4)    #O/P:- [9, 8, 7, 6, 5, 4]
print(nums)
nums.insert(2, 11) #O/P:-[9, 8, 11, 7, 6, 5, 4]
print(nums)
print(len(nums))   #O/P:-7