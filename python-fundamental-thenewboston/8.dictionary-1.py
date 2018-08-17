############### set ################

groceries = {'milk', 'cheese', 'butter', 'curd', 'milk'}
print(groceries)  # Even milk appears 2 times , but a set does not repeat it
print(groceries[0])  #TypeError: 'set' object does not support indexing


########### Dictionary ####################

name_id = {'Tony':'3001', 'Emma':'2032', 'Gary':'1032'}
print(name_id)

print(name_id['Tony']) #Only 1 id will be displayed...How about when 1000 Key - Value pair available

for k, v in name_id.items():
	print(k ," : ", v)
