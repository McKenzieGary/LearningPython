cars = 100 #this sets the variables cars equal to 100
space_in_a_car = 4.0 #4.0 is used because it is a floating point number in order to prevent rounding errors
drivers = 30 # this sets the variable drivers to 30
passengers = 90 # this sets the variable passengers to 90
cars_not_driven = cars - drivers # this sets the variable cars_not_driven equal to the variable cars minus the variable drivers
cars_driven = drivers #this sets the variable cars_driven equal to the number of drivers
carpool_capacity = cars_driven * space_in_a_car # this sets the variable carpool_capacity equal to cars_driven times space_in_a_car
average_passengers_per_car = passengers / cars_driven # this sets the variable average_passengers_per_car = equal to the variable passengers devided by the variable cars_driven


print("There are", cars, "cars available.") # this prints the string "There are" inserts the variable "cars" and then prints the string "cars available"
print("There are only", drivers, "drivers available.") # this prints the string "There are only" inserts the variable "drivers" and then prints the string "cars available"
print("There will be", cars_not_driven, "empty cars today.") # this prints the string "There will be" inserts the variable "cars_not_driven" and then prints the string "empty cars today"
print("We can transport", carpool_capacity, "people today.") # this prints the string "we can transport" inserts the variable "carpool_capacity" and then prints the string "people today."
print("We have", passengers, "to carpool today.") # this prints the string "we can transport" inserts the variable "passengers" and then prints the string "to carpool today."
print("We need to put about", average_passengers_per_car, "in each car.") # this prints the string "We need to put about" inserts the variable average_passengers_per_car and then prints the string "in each car"
