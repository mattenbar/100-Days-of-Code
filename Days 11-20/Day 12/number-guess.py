from random import randint

def play():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    attempts = 0

    if (difficulty == 'hard'):
        attempts = 5
    elif (difficulty == 'easy'):
        attempts = 10
    else:
        print("Sorry that is not a valid option.")

    number = randint(1, 100)

    while attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        if guess > number:
            print("Too high.")
            print("Guess again")
            attempts -= 1
        elif guess < number:
            print("Too low.")
            print("Guess again")
            attempts -= 1
        elif(guess == number):
            print("You win!")
            return 
play()