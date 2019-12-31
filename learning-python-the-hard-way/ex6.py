types_of_people = 10 # this sets the variable types_of_people equal to 10
x = f"There are {types_of_people} types of people." # this sets the variable x equal to the string "There are {types_of_people} types of people." and inserts the formated variable "types_of_people"

binary = "binary" # this sets the variable "binary" equal to "binary"
do_not = "don't" # this sets the variable "do_not" equal to "don't"
y = f"Those who know {binary} and those who {do_not}" # this function prints "Those who know {binary} and those who {do_not}" and inserts the formated variables "binary and "do_not"

print (x) # this function tells python to print the variable x
print (y) # this function tells python to print the variable y

print (f"I said:{x}") # this line prints "I said:" and inserts the formated variable x
print (f"I also said: '{y}'") # this line prints "I also said:" and inserts the formated variable y

hilarious = False # this line sets the variable hilarious equal to false
joke_evaluation = "Isn't that joke so funny?! {}" #this line sets the variable joke_evalutation equal to "Isn't that joke so funny?! {}"

print (joke_evaluation.format(hilarious)) #this line is telling python to print "joke evaluation and the formatted variable 'hilarious'"

w = "This is the left side of..." # this sets the variable w to equal ""This is the left side of...""
e = "a string with a right side." # this sets the variable e equal to "a string with a right side."

print(w + e) # this function prints the variable w plus the variable e (since its w+e w is printed before e)
