# Banker-Roulette-Who-will-Pay-the-Bill?

This Python script, titled "Banker Roulette - Who will Pay the Bill?", randomly selects a person from a list of names to determine who will pay for a meal. Here's a breakdown of how it works:

The script prompts the user to input names separated by commas using the input() function. The names are stored as a single string in the variable names_string.

The split() method is used to split the names_string into a list of individual names. Each name is separated by a comma.

The len() function is used to determine the number of items (names) in the names list.

The random.randint() function generates a random integer between 0 and the number of items in the list minus 1 (inclusive). This random integer represents the index of the person who will pay for the meal.

The script retrieves the name of the person who will pay by using the randomly generated index to access the corresponding element in the names list. This name is stored in the variable person_who_will_pay.

Finally, the script prints a message indicating which person will pay for the meal, using string concatenation to include their name in the output.

Overall, this script provides a simple and fair way to select a person at random from a group to pay for a meal, making it a fun game for deciding who covers the bill.
