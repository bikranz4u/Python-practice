#center() :-Returns a space-padded string with the original string centered to a total of width columns.
#Syntax-center(width, fillchar)
str=input("Enter a String: ")
print(str.center(10,'#'))

#count() :- count() method returns an integer that denotes number of times a substring occurs in a given string.
#           if starting index 'beg' and ending index 'end' are given.
#Syntax-count(str, beg= 0,end=len(string))
#
print('Count how many times a string occurs :-',str.count('test'))

print('Count how many times a string occurs within the index  :-',str.count('test',0, 15))