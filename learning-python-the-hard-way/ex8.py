formatter = "{} {} {} {}" #sets formatter variable to a series of four {}

print(formatter.format(1, 2, "3", "four" )) #inserts 1, 2, 3, 4 to associated {} in formatter variable and prints
print(formatter.format("one", "two", "three", "four")) # inserts "one", "two", "three", "four" to associated {} in formatter variable and prints
print(formatter.format(True, False, False, True)) # inserts True, False, False, True into associate {} in formatter variables and prints
print(formatter.format(formatter, formatter, formatter, formatter)) # inserts the "formatter" variable 4 times
print(formatter.format(
        "I will learn",
        "python",
        "to progress",
        "and achieve my dreams"
)) # inserts each string in associated formatter variable {}
