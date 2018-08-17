################# Unpacking Arguments #################

def health_calculator(age, apples_ate, cigs_smoke):
	ans = (100-age) + (apples_ate * 3.5) - (cigs_smoke * 2)
	print(ans)


input_data = [33, 1 , 0]
health_calculator(input_data[0],input_data[1],input_data[2])

health_calculator(*input_data) # We are calling all data 
