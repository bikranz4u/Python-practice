#The range function creates a sequential list of numbers.
#The call to list is necessary because range by itself creates a range object, 
# and this must be converted to a list if you want to use it as one.


#If range is called with one argument, it produces an object with values from 0 to that argument. 
numbers = list(range(5))
print(numbers)
#If it is called with two arguments, it produces values from the first to the second.

num = list(range(3, 8))
print(num)

print(range(20) == range(0, 20))


nums1 = list(range(5, 8))
print(len(nums1))

#range can have a third argument, which determines the interval of the sequence produced. This third argument must be an integer.
numbers = list(range(5, 20, 2))
print(numbers)