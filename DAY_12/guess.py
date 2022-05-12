import random

HARD_LEVEL= 5
EASY_LEVEL= 10

def difficulty():
  level_difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level_difficulty=="easy":
    return  EASY_LEVEL
  else:
    return HARD_LEVEL
    
def check_answer(answer,guess,turns):
  if guess<answer:
    print("Too low")
    return turns-1
  elif guess>answer:
    print("Too high")
    return turns-1
  else:
    print(f"You won the answer is {answer}")

def game():
  print("Welcome to the Number Guesing Game")
  print("I am thinking of  a number between 1 and 100")
  
  answer = random.randint(1,100)
  turns= difficulty()
  
  guess=0
  while guess!= answer:
    print(f"You have {turns} remaining")
    guess=int(input("Enter a guess: "))
    turns=check_answer(answer,guess,turns)
    if turns==0:
      print("You have run out of guesses")
      return 
    
game()
  
  
    
    