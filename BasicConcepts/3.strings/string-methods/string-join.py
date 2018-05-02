#Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
#Join () exactly takes one argument

List=['Sunny','Day']
output='-'.join(List)
print(output) #O/P:-Sunny-Day

#list=''.join('c','a','t')
#print(list)  #TypeError: join() takes exactly one argument (3 given)

list=''.join(['c','a','t'])
print(list)  #We will get no error as join tool a single argument, which is a list.
