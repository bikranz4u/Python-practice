"""Create borders for a string

Usage:

	python3  function_argument.py 
"""
#Function Argument

def banner(message, border='-'):
    """Creating border for a message.

	Args:
		Pass the value of first argument for message. A default argument(2nd argument) passed in the form of -.

	Returns:
		borders for a string
	"""
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Red Rose")

#Providing Optional Argument


banner("Petal Blue", "#")

#Providing Positional & Keyword argument (matched by name)

banner("Rasberry Pai", border="@")

#

banner(border=".", message="Rose Petals")


