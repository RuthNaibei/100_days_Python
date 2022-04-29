import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
guess = input("Guess a letter: ").lower()

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display=[]
for _ in range(len(chosen_word)):
  display += "_"
print(display)
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

for position in range(len(chosen_word)):
  letter=chosen_word[position]
  if letter==guess:
    display[position]=letter
print(display)