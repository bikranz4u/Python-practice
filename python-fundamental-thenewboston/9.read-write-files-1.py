########## Modules ###############

import test_module

test_module.test()   # We have referenced the module name infront of the function name.

################## How to Read and Write Files ################

# Writing to a file 
fw = open('sample.txt', 'w')      # Open the file with write mode

fw.write('Writing 1st line \n')   #Write the lines
fw.write('Writing 2nd Line')

fw.close()                        # Close the file, it will release the occupaid memories.

# Reading from a file
fr = open('sample.txt', 'r')      # Open the file with read mode
text = fr.read()
print(text)
fr.close()
