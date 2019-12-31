from sys import argv # this imports information from the command line

script, filename = argv #this sets the information from the command line to the variables script and filename

txt = open(filename) # this sets the variable txt to "open(filename)" which will open the file named the input from the command line

print(f"Here's your file {filename}:") # this formats the string and inserts the filename variable into it then prints
print(txt.read()) #this reads the txt variable (which was set to open filename) and then prints it

print("Type the filename again:") #this prints the string
file_again = input("> ") #this sets input from the user equal to the variable "file again"

txt_again = open(file_again) # this sets the variable txt_again equal to "open(fuile_again)" which will open the file set equal to the "file_again" variable that the user set

print(txt_again.read()) # this reads the variable "txt_again" and prints it.
