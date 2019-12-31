from sys import argv #imports the argv feature
from os.path import exists #imports the exists feature

script, from_file, to_file = argv #pulls input from command line and sets it equal to from_file and to_file

print(f"Copying from {from_file} to {to_file}") # inserts from_file and to_file into the formatted string and prints

# we could do these two on one line, how?
in_file = open(from_file) #opens from_file and sets it equal to in_file
indata = in_file.read() #sets indata equal to in_file in read mode

print(f"The input file is {len(indata)} bytes long") #reports the length of the indata file and inserts it into the formatted string

print(f"Does the output file exist? {exists(to_file)}") #asks if the to_file exists and plugs the answer into the formatted string and prints
print("Ready, hit RETURN to continue, CTRL-C to abort.") # prints the string
input() # asks for input from the user

out_file = open(to_file, 'w') #opens to_file in writing mode and sets it equal to out_file
out_file.write(indata) # writes the contents of indata in the out_file

print("Alright, all done.") # prints the string

out_file.close() # this closes the out file
in_file.close() # this closes the in file
