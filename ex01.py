# Ex01

# write here your function




s1= input("Enter first string:")
s2= input("Enter second string:")

def calculate_love_score(name1:str,name2:str) ->float:
    shared_values = set(name1) & set(name2)
    average_length = (len(name1) + len(name2)) / 2
    love_score = (len(shared_values) / average_length) * 100
    return love_score

write = calculate_love_score(s1,s2)
# test your function 
print(f"The love score between {s1} and {s2} is {write:.1f}%")


