def add(a, b): # this defines the add function using arguments a and b (these are 'arguments')
    print(f"ADDING {a} + {b}") # this sets the add function equal to printing the formatted string and inserting the variables a and b
    return a + b # this returns the result of a + b

def subtract(a, b): # this defines the subtract function using arguments a and b
    print(f"SUBTRACTING {a} - {b}") # this sets the subtract function equal to printing the formatted string and inserting the variables a and b
    return a - b # this returns the result of a - b

def multiply(a, b): # this defines the multiply function using arguments a and b
    print(f"MULTIPLYING {a} * {b}") # this sets the multiply function equal to printing the formatted string and inserting the variables a and b
    return a * b # this returns the result of a * b

def divide(a, b): # this defines the divide function using arguments a and b
    print(f"DIVIDING {a} / {b}") # this sets the divide function equal to printing the formatted string and inserting the variables a and b
    return a / b # this returns the results of a / b


print("Let's do some math with just functions!") # this prints the string

age = add(30, 5) # this sets the age variable equal to the add function using the parameters 30 and 5
height = subtract(78, 4) # this sets the height variable equal to the substract function using the parameters 78 and 4
weight = multiply(90, 2) # this sets the weight variable equal to the multiply function using the parameters 90 and 2
iq = divide(100, 2) # this sets the iq variable equal to the divide function using the parameters 100 and 2

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}") # this prints the formatted string and inserts all of the variables calculated above


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.") # this prints the string

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # this is weird because it prints out each function on its own line

print("that becomes: ", what, "Can you do it by hand?") # I did it by hand! it came out to -4391
