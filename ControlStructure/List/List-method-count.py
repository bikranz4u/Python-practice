#list.count(obj): Returns a count of how many times an item occurs in a list

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.count('r'))  #O/P:-1
print(letters.count('p'))  #O/P:-2  # index method finds the "first occurrence" of a list item and returns its index
print(letters.count('z'))  #O/P:-0