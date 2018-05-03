#find(str, beg=0 end=len(string))
#Determine if str occurs in string or in a substring of string if starting index beg and 
#ending index end are given returns index if found and -1 otherwise.
str=input("Enter a String: ")
print(str.find('Best'))

#index(str, beg=0, end=len(string))
#Same as find(), but raises an exception if str not found.
print(str.index('BEST'))   #If String not found then #ValueError: substring not found
