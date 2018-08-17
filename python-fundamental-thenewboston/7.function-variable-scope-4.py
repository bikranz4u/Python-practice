################## Variable Scope #####################

a = 1234

def func1():
	b = "Local to Func1"
	print("GOBAL VARIABLE", a)
	print(b)
	print(c)  #name 'c' is not defined, This will happen as Variable c is local to func2, can't  be accessed in func1.
	

def func2():
	c = "local to func2"
	print("GOBAL VARIABLE", a)
	print(b) #NameError: name 'b' is not defined , This will happen as Variable b is local to func1, can't be accessed in func2.
	print(c)

    

func1()
func2()
