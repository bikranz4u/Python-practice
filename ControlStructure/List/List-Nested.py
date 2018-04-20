#Lists can also be nested within other lists.
#Lists of lists are often used to represent 2D grids, 
#as Python lacks the multidimensional arrays that would be used for this in other languages.

number = 100
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])    #O/P:-0
print(things[2])    #O/P:-[1,2,number]
print(things[2][2]) #number


list = [42, 55, 67]
print("The 2nd item in the List is: ",list[2])