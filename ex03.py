# Ex03
3
""""Program the function select_random_gift with one parameter: a dictionary of wishlists. The function randomly selects a gift
for each person from their wishlist. It returns the result as a dictionary. In each case, the person's name is the key and the
chosen gift is the value. After the dictionary is returned, print key & value as below."""""
import random
# write here your function
def select_random_gift(wishlist:dict[str,str]) -> dict[str,str]:
    my_dict = {}
    for person, gifts in wishlist.items():
        random_gift = random.choice(gifts)  # Selects one gift from the person's wishlist
        my_dict[person] = random_gift      # Adds it to the dictionary with the person's name as the key
    return my_dict




# test your function
dict_wishlists_persons = { "Stijn":["Bike", "Headphones", "Fitbit"], "Marie": ["Game", "Bike", "Screen", "Swimming band"], "Joerie": ["Racing bike", "Swimming band", "Book"], "Henk":["Laptop", "Beer Omer", "Bike"]}
print("Each person is randomly given a gift from their wish list.\nThis is the result:")
# ...
random_gift = select_random_gift(dict_wishlists_persons)
for person, gift in random_gift.items():
    print(f"{person} -> {gift}")