# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
if size=="S":
  if add_pepperoni=="Y":
    bill+=15
    bill += 2
  else:
    bill+=15
elif size=="M":
  if add_pepperoni=="Y":
    bill+=20
    bill+=3
  else:
    bill+=20
elif size=="L":
  if add_pepperoni=="Y":
    bill+=25
    bill+=3
  else:
    bill+=25
    
if extra_cheese=="Y":
    bill+=2

print(f"Your final bill is: ${bill}")
  
  
  
  


  
  
  
