from sys import argv

baller = argv

filename = input("Want me to empty your file buddy? Go ahead and tell me the filename: ")

print(f"Here, read your file one last time:")
clearjob = open(filename)
print(clearjob.read())

print(f"Now watch it disappear")

clearjob = open(filename, 'w')
clearjob.truncate()

print(f"See, nothing left in your file homes.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

clearjob.write(line1)
clearjob.write(line2)
clearjob.write(line3)

print(f"Here is the result: ")
clearjob = open(filename)
print(clearjob.read())
