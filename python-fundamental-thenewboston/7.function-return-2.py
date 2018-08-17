#################### Function Return ###########################

def allowed_dating_age(boy_age):
	girls_age = boy_age/2 + 7
	return girls_age

# Lets assign the return value to a variable
limit = allowed_dating_age(32)

print("The Boy of age " ,boy_age, "should date a girl of age " ,limit, "or older")
