from sys import argv # this imports argv from the sys
#read the wyss section for how to run This
script, first, second, third = argv # this sets argv to script, first, second, third

print("The script is called:", script) # this prints the string and then inserts the script variable from the command line into this
print("Your first variable is:", first)# this prints the string and then inserts the first variable from the command line
print("Your second variable is:", second) # this prints the string and then inserts the second variable from the command line
print("Your third variable is:", third) # this prints the string and then inserts the third variable from the command line


print ("how old are you?", end = ' ') # this prints the string "How old are you" and then goes to the next line for input
age=input() # this asks for more input
