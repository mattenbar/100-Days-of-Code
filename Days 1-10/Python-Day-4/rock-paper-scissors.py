import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computerChoice = random.choice([0, 1, 2])

if userChoice == 0:
  print(rock)
if userChoice == 1:
  print(paper)
if userChoice == 2:
  print(scissors)

print("Computer chose:")
if computerChoice == 0:
  print(rock)
if computerChoice == 1:
  print(paper)
if computerChoice == 2:
  print(scissors)

if userChoice < 0 or userChoice > 2:
  print("You typed an invalid number, you lose!")
else:
  if(userChoice == 0 and computerChoice == 2):
    print("You win")
  elif(userChoice == 1 and computerChoice == 0):
    print("You win")
  elif(userChoice == 2 and computerChoice == 1):
    print("You win")
  elif(userChoice == computerChoice):
   print("It's a draw")
  else:
    print("You lose")