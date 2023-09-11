from art import logo
import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def total_score(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return(sum)

def print_cards(arr):
    card_string = ''
    for i in arr:
        card_string += f"{i}, "
    return card_string[:len(card_string)-2]

def check_if_over(arr):
    if total_score(arr) > 21:
        return True
    else:
        return False

def computer_hand(first_card):
    computer_cards =[first_card]
    computer_cards.append(random.choice(cards))

    while total_score(computer_cards) < 18:
        computer_cards.append(random.choice(cards))

    return computer_cards

def get_winner(player_cards, computer_card_1):
    comp_cards = computer_hand(computer_card_1)
    player_total = total_score(player_cards)
    comp_total = total_score(comp_cards)
    print(f"Your final hand: [{print_cards(player_cards)}], final score: {total_score(player_cards)}")
    print(f"Computer's final hand: [{print_cards(comp_cards)}], final score: {total_score(comp_cards)}")

    if player_total > 21 and comp_total > 21:
        print("You both bust. It's a Draw")
    elif player_total > 21 and comp_total <= 21:
        print("You went over. You lose 😭")
    elif player_total <= 21 and comp_total > 21:
        print("Computer went over. You Win!")
    else:
        if player_total > comp_total:
            print("You win!")
        else:
            print("Computer wins")

def blackjack():
    continue_playing = True
    print(logo)
    player_card_1 = random.choice(cards)
    player_card_2 = random.choice(cards)
    player_cards = [player_card_1, player_card_2]
    computer_card_1 = random.choice(cards)
        
    while continue_playing:
        print(f"Your cards: [{print_cards(player_cards)}], current score: {total_score(player_cards)}")
        print(f"Computer's first card: {computer_card_1}")
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_cards.append(random.choice(cards))
            if (check_if_over(player_cards)):
                get_winner(player_cards, computer_card_1)
                continue_playing = False
        else:
            get_winner(player_cards, computer_card_1)
            continue_playing = False
    
    if input("Do you want to play another game of Blackjack? Type 'y' or 'n': ") == 'y':
        blackjack()

        
            
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

