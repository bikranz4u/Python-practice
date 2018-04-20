#The index method finds the "first occurrence" of a list item and returns its index.
# If the item isn't in the list, it raises a "ValueError".
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))  #O/P:-2
print(letters.index('p'))  #O/P:-0  # index method finds the "first occurrence" of a list item and returns its index
print(letters.index('z'))  #O/P:-ValueError: 'z' is not in list

