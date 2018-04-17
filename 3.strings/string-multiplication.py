#Strings can also be multiplied by integers. This produces a repeated version of the original string.
# The order of the string and the integer doesn't matter, but the string usually comes first.

print("spam" * 3) #O/p:spamspamspam
print (4 * '2')   #O/p: 2222

#Strings can't be multiplied by other strings. 
#Strings also can't be multiplied by floats, even if the floats are whole numbers.

print ('17' * '87') #TypeError: can't multiply sequence by non-int of type 'str'
print ( 'pythonisfun' * 7.0) #TypeError: can't multiply sequence by non-int of type 'float'