import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# def computer_turn():
#     computer_score = 0
#     while True:
#         die_value = roll()
#         if die_value == 1:
#             computer_score = 0
#             print("Computer rolled a 1! Computer score reset to 0")
#             return computer_score
#         else:
#             computer_score = computer_score + die_value
#             print(f"Computer rolled a {die_value}. Computer Score: {computer_score}")
#             print("Computer, do you want to play again?")
#             comp_continue = random.randint(1,20)
#             if comp_continue <= 15: # Giving computer more of a chance to cotinue
#                 print("Computer wishes to continue")
#                 continue
#             else:
#                 print(f"Computer do not want to continue. Computer Score: {computer_score}")
#                 return computer_score

def computer_turn(computer_score):

    while True:
        if computer_score >= 20:
            return computer_score

        die_value = roll()

        if die_value == 1:
            computer_score = computer_score - computer_score
            print("Computer rolled a 1. Computer score reset to 0")
            return computer_score

        computer_score = computer_score + die_value
        print(f"Computer score is {computer_score}")
        comp_continue = random.randint(1,10)
        if comp_continue <= 5:
            continue
        else:
            return computer_score


def user_turn(user_score):

    while True:
        if user_score >= 20:
            return computer_score
        
        die_value = roll()
        print(f"You rolled a {die_value}.")

        if die_value == 1:
            user_score = user_score - user_score
            print("You rolled a 1. Your score is reset to 0!")
            return user_score
        
        user_score = user_score + die_value
        print(f"Your score is {user_score}")

        reply = input("Do you wish to continue: y/n").lower()
        if reply == "y":
            continue
        else:
            return user_score
            

        # while True:
        #     
        #     if die_value == 1:
        #         user_score = 0
        #         print("Computer rolled a 1! Computer score reset to 0")
        #         return user_score
        #     else:
        #         break



##### My code: Wasn't working. Was only allowing the user to play
# while True: # Game playing
#     while True: # User Playing, initial
#         user_score = user_turn()
#         if user_score != 0 and user_score < 20:
#             continue
#         elif computer_score == 0:
#             break # Go to external while, let computer play
#         elif user_score >= 20: 
#             print(f"You win with {user_score} points")
#             break
#         break
#     while True: # If user score = 0, computer plays
#         computer_score = computer_turn()
#         if computer_score != 0 and user_score < 100:
#             continue
#         elif computer_score == 0:
#             break # Go to external while, let user play
#         elif computer_score >= 100:
#             print(f"Computer wins with {computer_score} points!")
#             break
#         break


# Code with help from online
while True: 
    user_score = 0
    computer_score = 0

    while True:
        user_score += user_turn(user_score)
        if user_score == 0:
            print("Computer's turn")
            break

        if user_score >= 20:
            print(f"You win! You scored {user_score}. Computer score: {computer_score}")
            quit()
            
    while True:
        computer_score += computer_turn(computer_score)
        if computer_score == 0:
            print("Your turn!")
            break
            
        if computer_score >= 20:
            print(f"Computer wins! Computer scored {computer_score}. Your score: {user_score}")
            quit()

