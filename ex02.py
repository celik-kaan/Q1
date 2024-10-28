# Ex02
"""Write the function ‘make_couples’. The function takes two parameters. The first parameter is a list of unique names. The
second parameter is the desired number of couples. The function returns a dictionary: each item represents a unique couple
of names (you use the first name as the key, the second name as the value). The number of couples in the dictionary
matches the number you requested.
The function first checks whether the requested number of pairs can be formed. Then it makes all the pairs: choose two
different people from the list each time. Add them to the dictionary. Make sure that the same person is not chosen twice.
Finally, return the dictionary."""
import random

# write here your function
def make_couples(unique_names: list[str], number_couples: int) -> dict[str, str]:    
    # Check if enough unique pairs can be created
    if number_couples > len(unique_names) // 2:
        return "Not enough unique names to form the requested number of couples."

    
    # Dictionary to store the couples
    my_dict = {}
    available_names = unique_names[:]  # Copy list to avoid modifying the original
    
    for i in range(number_couples):
        # Select two different people from the list
        random_key = random.choice(available_names)
        available_names.remove(random_key)  # Remove to avoid choosing the same person again

        random_value = random.choice(available_names)
        available_names.remove(random_value)

        # Add the couple to the dictionary
        my_dict[random_key] = random_value

    return my_dict

# test your function 
print("💘 The couples of Howest are 💘")
students = ["Karel", "Ben", "Tim", "Ken", "Henk", "Lies", "Barbie", "Sandra", "Debbie"]
number_couples = int(input("How many couples should be formed?:> "))


testing = make_couples(students, number_couples)
print(f"💘 The couples of Howest are 💘 {testing}")