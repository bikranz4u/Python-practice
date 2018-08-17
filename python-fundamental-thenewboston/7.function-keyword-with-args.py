############# Keyword Arguments ###################

def sentence(name="Arman", job='testing', action='loves'):  # Default Argument
	print(name, action, job)

sentence()   #This will call the default argument

sentence(name='Sally', action='hates') # We have overridden the default value 

sentence(name='Randy', job='architecting') # We have overridden the default value
