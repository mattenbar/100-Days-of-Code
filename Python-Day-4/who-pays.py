# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_of_names = len(names) - 1

rand_num = random.randint(0, number_of_names)

print(f"{names[rand_num]} is going to buy the meal today!")