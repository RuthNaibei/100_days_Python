# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
test_seed= int(input("Create a seed number: "))
random.seed(test_seed)

names= names_string.split(",")

len_names= len(names)
who_pays=random.randint(0,len_names-1)
person=names[who_pays]

print(f"{person} is going to buy the meal today!")