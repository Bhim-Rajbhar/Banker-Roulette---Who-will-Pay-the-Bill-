########### Banker Roulette - Who will Pay the Bill ? #######################

import random  # Importing the random module to generate random choices

# Prompting the user to input names separated by commas
names_string = input("Give me everybody's name separated by a comma(,) :\n")

# Splitting the input string into a list of names using the comma as a delimiter
names = names_string.split(",")

# Getting the number of items (names) in the list
num_items = len(names)

# Generating a random integer between 0 and the number of items in the list minus 1
random_choice = random.randint(0, num_items - 1)

# Selecting a random person from the list based on the randomly generated index
person_who_will_pay = names[random_choice]

# Printing the selected person who will pay for the meal
print(person_who_will_pay + " is going to buy the meal today!")
