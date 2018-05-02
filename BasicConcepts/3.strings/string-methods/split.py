#Splits string according to delimiter string, returns list of substrings.
#Default delimiter is ' ' .

str='Test My Skill'
output=str.split()
print(output)     #o/p:- ['Test', 'My', 'Skill']

for x in output:
    print(x)      #o/p:-Test
                  #     My
                  #     Skill

#Delimiter can be changed in the split() argument

str="02-May-2018"
output=str.split('-')
for x in output:
    print(x)


time="12:00:05"
output=time.split(':')
for x in output:
    print(x)

