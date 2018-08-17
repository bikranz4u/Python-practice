######### Flexible Number of Arguments ###########
#We can allow undefined number of variables


def add_numbers(*args):  # *used to access n number of variables 
	total =0 
	for a in args:
		total += a
	print(total)


add_numbers()
add_numbers(5,6,7)
add_numbers(43,9,98,134)
