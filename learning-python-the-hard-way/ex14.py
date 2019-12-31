from sys import argv #this imports variables set to argv from command line

script, user_name, age = argv # this sets argv equal to script, user_name, and age
prompt = '> ' #this sets the variable prompt equal to '> '

print(f"Hi {user_name}, I'm the {script} script.")# this formats the variables username and script and inserts them into the string then prints
print(f"I see you are {age} years old. Congratulations, that's old enough to play this game")# this formats the variable age and inserts it into the string then prints
print("I'd like to ask you a few questions.")# this prints the string
print(f"Do you like me {user_name}?")# this formats the variable user_name and prints the string
likes = input(prompt) #this sets the variable likes to the input provided

print(f"Where do you live {user_name}?")
lives = input(prompt)
#this prints a question and then promts the user for input
print("What kind of computer do you have?")
computer = input(prompt)
#this formats the variables likes,lives,computer and inserts them into the string and prints it
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
and you have a {computer} computer. Nice.
""")
