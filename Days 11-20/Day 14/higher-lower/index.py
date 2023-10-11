import art
import game_data
import random



def getPeopel():
    firstNum = random.randint(0, len(game_data.data)-1)
    secondNum = random.randint(0, len(game_data.data)-1)

    while firstNum == secondNum:
        secondNum = random.randint(0, len(game_data.data)-1)


    return {'A':game_data.data[firstNum],'B':game_data.data[secondNum]}



continuePlaying = True
score = 0

print(art.logo)
people = getPeopel()

while continuePlaying:
    
    print(f'Compare A: {people["A"]["name"]}, a {people["A"]["description"]}, from {people["A"]["country"]}')
    print(art.vs)
    print(f'Compare B: {people["B"]["name"]}, a {people["B"]["description"]}, from {people["B"]["country"]}')
    guess = input("Who has more followers? Type 'A' or 'B': ")
    
    if guess == 'A' and people["A"]["follower_count"] > people["B"]["follower_count"]:
       score += 1
       print(art.logo)
       print(f'Your\'re right! Current score: {score}.')
       people = getPeopel()
    elif guess == 'B' and people["A"]["follower_count"] < people["B"]["follower_count"]:
        score += 1
        print(art.logo)
        print(f'Your\'re right! Current score: {score}.')
        people = getPeopel()
    else:
        print(art.logo)
        print(f'Sorry, that\'s wrong. Final score: {score}')
        continuePlaying = False
 
    
