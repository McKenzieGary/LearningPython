print("How old are you?", end=' ')#prints the string "hold old are you?" and moves the next print to the line below it
#if you dont have end=' ' here, the variable is entered below the string instead of beside it.
age = input() #asks someone to set the age variable
print("How tall are you?", end=' ') # prints the string "how tall are you?" and moves the next print to the line below it
height = input() #asks someone to set the height variable
print("How much do you weigh?", end=' ')# prints the string "how much do you weigh" and moves the next print to the line below it
weight = input() #asks someone to set the weight variable
#formats the variables and prints the string and inserts the age, height and weight variables
print(f"So, you're {age} years old, {height} tall and {weight} heavy.") #formats the string and inserts the variables age,height,weight into the string.


print ('Enter your name :')
x = input()
print ('Hello, ' + x)
