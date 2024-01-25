import random

total_games = 0
user_wins = 0
computer_wins = 0
ties = 0

while True:
    user_input = input("\nType \"Rock\", \"Paper\" or \"Scissors\" or \"Q\" to quit:\n> ").lower()

    if user_input == "q":
        break
    
    total_games += 1

    if user_input in ["rock", "paper", "scissors"]:
        options = ["rock", "paper", "scissors"]
        random_int = random.randint(0, 2)
        computer_input = options[random_int]
        print(f"Computer chose: {computer_input.capitalize()}")

        if user_input == computer_input:
            ties += 1
            print("Tie!")
            continue
        
        elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
            print(f"You win! {user_input.capitalize()} beats {computer_input.capitalize()}!")
            user_wins += 1
            continue
        
        else: 
            print(f"Computer wins! {computer_input.capitalize()} beats {user_input.capitalize()}")
            computer_wins += 1
            continue

    else: 
        print("Invalid option! Try again")
        continue

print("Results:")
print(f"User wins: {user_wins} \t Computer wins: {computer_wins} \t Ties: {ties} \t Total games: {total_games}")