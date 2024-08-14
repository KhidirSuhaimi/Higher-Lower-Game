import game_data
import random
import funct

#Create a game that compares 2 entities
# eg Compare Name, a description, from where
# Compares the number of followers

#Random choice , but cannot be the same
#if same , find again
# Compare follower count
# If correct, print ( Correct + current score)
#If Wrong, say Sorry thats wrong. Final Score: {score}



lose = False
def check(A,B):
    if A['follower_count'] > B['follower_count']:
        return 'A'
    else:
        return 'B'

def is_correct(answer,decision):
    if answer == decision:
        return True
    else :
        return False


score = 0
while not lose :

    if score != 0:
        print(f"Youre right! Current Score: {score}")

    firstChoice = random.choice(game_data.data)
    secondChoice = random.choice(game_data.data)
    while secondChoice == firstChoice:
        secondChoice = random.choice(game_data.data)
    print(f"Compare A : {firstChoice['name']}, a {firstChoice['description']}, from {firstChoice['country']} {firstChoice['follower_count']}")
    print(f"Compare B : {secondChoice['name']}, a {secondChoice['description']}, from {secondChoice['country']} {secondChoice['follower_count']}")
    answer = check(firstChoice,secondChoice)
    decision = funct.get_user_input()
    final = is_correct(answer,decision)

    if final:
        score += 1
        print("\n"*10)
    else:
        print(f"Sorry that is wrong.Final score {score}")
        lose = True




