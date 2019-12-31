# this one is like your scripts with argv
def print_two(*args): #this begins to define the print_two function using the args we will assign later
    arg1, arg2 = args # this sets *args equal to arg1, arg2 in order
    print(f"arg1: {arg1}, arg2: {arg2}") # this prints the formatted string and insterts arg1 and arg2 which we will assign when we call the function.

#ok, that *args is actually pointless we can just do This
def print_two_again(arg1, arg2): #this defines the print two again function and tells the function to use the arg1, arg2 variables we assign later
    print(f"arg1: {arg1}, arg2: {arg2}") # this inserts the variables we assign when we call the function.

# this just takes one argument
def print_one(arg1): #initiates the definition of the print_one function using one variable set to arg1
    print(f"arg1: {arg1}") #prints the formatted string and inserts the arg1 variable (which we will set later when we call the function)

#this one takes no arguments
def print_none(): # initiates the definition of print_one function
    print("I got nothin'.") #sets the print_one function to print "I got nothin'." when called


print_two("Zed","hello") #performs the print_two function setting arg1 to zed and arg 2 to shaw ****if both arguments arent here when the defined function says there will be two variables the script doesnt work.
print_two_again("Zed","Shaw") #performs the print_two_again function setting arg 1 to zed and arg2 to shaw
print_one("First!") # performs the defined print_one function setting arg1 equal to first!
print_none() #performs the defined print_none function
