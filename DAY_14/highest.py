from game_data import data
from art import logo,vs
import random
from replit import clear

print(logo)
score=0

should_continue=True
account_b=random.choice(data)

while should_continue:
  def random_choice(account):
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    
    return(f"{account_name}, a {account_description}, from {account_country}")
  
  #check answer function
  def check_answer(guess, a_followers,b_followers):
    if a_followers>b_followers:
      return guess=="a"
    else:
      return guess=="b"
    
  account_a=account_b
  account_b=random.choice(data)
  
  
  if account_a == account_b:
    account_b=random.choice(data)
  
  print(f"Compare A: {random_choice(account_a)}")
  
  #print logo
  print(vs)
  
  print(f"Compare B: {random_choice(account_b)}")
  
  #user input
  
  guess= input("Who has more followers? Type 'A' or 'B':").lower()

  #get the number of followers
  a_followers=account_a["follower_count"]
  b_followers=account_b["follower_count"]
  
  is_correct=check_answer(guess,a_followers,b_followers)
  #clears screen
  clear()
  print(logo) 
  
  if is_correct:
    score+=1
    print(f"You are right current score is {score}")
  else:
    should_continue=False
    print(f"You are wrong . Final score is {score}")
