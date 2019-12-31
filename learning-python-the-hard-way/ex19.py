amount_of_cheese = 10 # this sets the parameter of cheeses to 10
amount_of_crackers = 50 # this sets the parameter of crackers to 50

def cheese_and_crackers(cheese_count, boxes_of_crackers):#this defines the function cheese_and_crackers and sets the parameters to cheese_count and boxes_of_crackers
    print(f"You have {cheese_count} cheeses!") # this tells the defined function to print the formatted string and insert the variables
    print(f"You have {boxes_of_crackers} boxes of crackers!") #this tells the defined function to print theformatted string and insert the variables
    print("Man that's enough for a party!") # this tells the defined function to print the string
    print("Get a blanket.\n") # this tells the function to print the string and then go to the next line


print("We can just give the function numbers directly:") # this prints the string
cheese_and_crackers(20, 30) #This prints the defined function plugging in 20 and 30 for cheese_count, boxes_of_crackers respectively


print("OR, we can use variables from our script:") # this prints the string


cheese_and_crackers(amount_of_cheese, amount_of_crackers) # this prints the defined function from above using the variables in the paranthesis


print("We can even do math inside too:") # this prints the string
cheese_and_crackers(10 + 20, 5 + 6) # this tells python to run the defined function cheese_and_crackers and sets the paramters cheese_count and boxes_of_crackers to the equations in order


print("And we can combine the two, variables and math:") # this prints the string
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)# this tells python to run the defined function and then add numbers to the defined parameters

test1 = 10
test2 = 50
def this_is_a_test (test1, test2):
    print(f"I am testing if I can make this function run with {test1}, and {test2}")
    print (f"I set {test1} equal to 10 and {test2} equal to 50")

this_is_a_test (test1, test2)

print ("but below I've added 50 to test1 and 10 to test2 to make them equal eachother")

this_is_a_test (10 + 50, 50 + 10)
