#Step 1 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
wordArr = [*word]

wordLength = len(wordArr)

userGuess = []
for _ in range(len(wordArr)):
    userGuess.append('_')


guesses_left = 6

print("Lets play hangman!")

while guesses_left > 0 and bool('_' in userGuess):
    userInput = input("Guess a letter: ").lower()
    while not len(userInput) == 1 :
        userInput = input("Guess 1 letter at a time: ").lower()

    if userInput in wordArr:
        for itr in range(wordLength):
            if wordArr[itr] == userInput:
                userGuess[itr] = userInput
        print(''.join(userGuess))
    else:
        guesses_left -=1
    print(stages[guesses_left])
    

if guesses_left  < 5 and bool('_' not in userGuess):
    print("You won!")
else:
    print("You lose :'( ")