#Pass by Object Reference
#The value of the reference is copied , not the value of the object
# Helpful Link https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

m = [9, 15, 24]
def modify(k):
    """Appending a value to function.

	Args:
		A any literal can be added.

	Returns:
		If you want to modify a copy of a object it the responsiblity of the function to do the coping it. The literal will be appended at the end of the list.
	"""
    k.append(41)
    print("Value of k =", k)


print("Value of m before function call=", m)

modify(m)

print("Value of m after function call=", m)


# 


#
f = [9, 15, 24]
def replace(g):
    """Creating a new list.

	Args:
		A any literal can be added.

	Returns:
		If you want to modify a copy of a object it the responsiblity of the function to do the coping it. The literal will be appended at the end of the 
    """
    g = [17, 22, 35]
    print("Value of g =", g)

print("Value of f before function call=", f)

replace(f)

print("Value of f after function call=", f)

