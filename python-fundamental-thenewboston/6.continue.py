###############. Continue. ####################

available=[2,5,8,11]

print(" Booking Status ")

for num in range(20):
	if num not in available:
		print(num," Booked ")
		continue
	else:
		print(num," Available ")

'''
# #########Try to implement something like ticketing system  
print("Available Seats",available)
booking = input ("Select a seat from available :- " )
available = 
'''
