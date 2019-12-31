# This script requires you to make a file before executing the script.
from sys import argv#this inputs argv from command line

script, input_file = argv # this sets command line variables to script and input_file

def print_all(f): #this defines the print all function and inserts a file parameter (f)
    print(f.read())# this sets the defined print all function to read the file (f) and print it

def rewind(f): #this defines the function 'rewind' and plugs in the f file parameter
    f.seek(0) # this sets the defined rewind function to seek byte 0 in the f file

def print_a_line(line_count, f): # this defines the function print a line and plugs in the parameters line_count and the file f
    print(line_count, f.readline()) # this sets the defined function print a line equal to read the file f and print the line count (readline is its own function already coded)

current_file = open(input_file) # this sets the variable current_file equal to the function of opening the input file from the command line variable

print("First let's print the whole file:\n") # this prints the string and goes to the next line

print_all(current_file) # this performs the print_all function on the Current_file paramater which was defined in line 14

print("Now let's rewind, kind of like a tape.") # this prints the string

rewind(current_file) # this performs the rewind function on the current_line parameter

print("Let's print three lines:") # this prints the string

current_line = 1 # this sets the current line equal to line 1
print_a_line(current_line, current_file) # this performs the print a line function with the parameters current line and current file

current_line = current_line + 1 # this adds 1 to the old current line variable and sets it equal to a new current line variable
print_a_line(current_line, current_file) # this performs the print a line function with the parameters current line (the new one) and current file

current_line = current_line + 1 # this adds 1 to the second current line variable and sets it equal to a new, third, current line variable
print_a_line(current_line, current_file) # this performs the print a line with the new current line parameter and the current file parameter
