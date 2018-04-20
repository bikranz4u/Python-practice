#The item at a certain index in a list can be reassigned.

#In the below example , we are re-assigned List[2] to "Bull"
nums = [7, 8, 9, 10, "spring"]
nums[2] = "Bull"
print(nums)
print("===================================")
#What is the result of this code?
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]       # We are re-assigning nums[3] = 2
print(nums[3])

print(nums + [4, 5, 6])
print(nums * 3)

print("===================================")
##Lists can be added and multiplied in the same way as strings.
nums = [1, 2, 3]
nums2 = [11,22,33]

#print("nums * nums2", nums * nums2) #TypeError:can't multiply sequence by non-int of type 'list'
print(nums[1] * nums2[1])  # We have multiplied 2 numbers.

char = ["a","b","c"]
char2 = ["x","y","z"]

print ("char + char2", char + char2)
#print ("char * char2", char * char2)  #TypeError:can't multiply sequence by non-int of type 'list'

print("Multiplying Number with Character list",nums[2]*char)  # O/p:-2 * [a,b,c]=[a,b,c,a,b,c]
print("Multiplying indexed Number with Character index list",nums[2]*char[2]) #O/P:- ccc


#Lists and strings are similar in many ways - strings can be thought of as lists of characters that can't be changed.