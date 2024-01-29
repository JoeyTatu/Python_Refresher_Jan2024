import random

def roll() -> int:
    die_value = random.randint(1, 6)
    return die_value

while True:
    players = input("Number of players: ")
    
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be 2 - 4 players")
    else:
        print("invalid number, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    
    for player_idx in range(players):
        print(f"Player {player_idx + 1}'s turn")
        print(f"Your total score is {player_scores[player_idx]}")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)? ").lower()
            if should_roll != "y":
                break
            
            die_value = roll()
            if die_value == 1:
                print("You rolled a 1! Turn ended!")
                current_score = 0
                break
            else:
                current_score += die_value
                print(f"You rolled a {die_value}")
            
            print(f"Your score is {current_score}")
        
        player_scores[player_idx] += current_score
        print(f"Your total score is {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player {winning_idx} is the winner with a score of {max_score}")