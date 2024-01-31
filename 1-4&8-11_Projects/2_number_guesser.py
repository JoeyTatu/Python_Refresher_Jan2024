import random

# start = -5
# stop = 11
# r = random.randrange(start, stop)
# r = random.randint(start, stop)
# print(r)

top_of_range = input("Type a number:\n> ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number")
    quit()

random_number = random.randint(0, top_of_range)
# print(random_number)

guesses = 0

# while user_guess != random_number:
while True:
    guesses += 1
    
    user_guess = input("Enter your guess:\n> ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue

    if user_guess > top_of_range:
        print(f"Number too high. Max number is {top_of_range}!")
        continue
    
    if user_guess <= 0:
        print("Please type a number greater than 0")
        continue
    
    if user_guess != random_number:
        print("Incorrect! Try again!")
        continue

    else:
        print("Correct! Well done!")
        print(f"You got it in {guesses} guesses!")
        break
