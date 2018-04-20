#list.reverse(): Reverses objects in a list
#reverse method does not take any argument.
nums = [1, 2, 3, 5, 6, 7]
print (nums.reverse())  #O/P:-None
print(nums)             #[7, 6, 5, 3, 2, 1]
#Note:-The reverse() method modifies the sequence in place for economy of space when reversing a large sequence. 
#      To remind users that it operates by side effect, it does not return the reversed sequence. 


letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.reverse())  #O/P:-None

print(letters)    #['u', 'p', 's', 'r', 'q', 'p']