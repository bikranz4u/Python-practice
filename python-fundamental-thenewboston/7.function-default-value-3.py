############## Default Values for Arguments #######################

def get_gender(sex='unknown'):
	if sex is 'm':
		sex = 'Male'
	elif sex is 'f':
		sex = 'female'
	print(sex)

get_gender('m')
get_gender('f')
get_gender()
