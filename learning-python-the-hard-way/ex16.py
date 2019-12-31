from sys import argv #imports variables from command line into script

script, filename = argv #sets command line variables equal to script and filename

print(f"We're going to erase {filename}.") #formats string and inserts variable filename
print("If you dont what that hit CTRL-C (^C).")#prints string
print("If you dont want that, hit RETURN.")#prints string

input("?")#if press return goes to next line if press ctrl c everything stops instantly

print("Opening the file...") #prints string
target = open(filename, 'w') # opens file just created called filename and sets the opened file equal to target

print("Truncating the file. Goodbye!") #prints string
target.truncate() #deletes the contents of the variable target - in this case its an open file named filename

print("Now I'm going to ask you for three lines.") # prints string

line1 = input("line 1: ") # requires input from user and sets that equal to variable line 1
line2 = input("line 2: ") # requires input from user and sets that equal to variable line 2
line3 = input("line 3: ") # requires input from user and sets that equal to variable line 3

print("I'm going to write these to the file.") # prints string

target.write(line1) #writes variable line 1 in target (which is the open file named filename)
target.write("\n") #moves to the next line
target.write(line2) #writes variable line 2 in target (which is the open file named filename)
target.write("\n") #moves to the next line
target.write(line3) #writes variable line 3 in target (which is the open file named filename)
target.write("\n") #moves to next line


print("And finally, we close it.") #prints string
target.close() #closes variable target which is equal to the opened file named filename
