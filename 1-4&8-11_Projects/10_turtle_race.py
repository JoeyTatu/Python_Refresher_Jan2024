import turtle
import time
import random

#CONSTS
WIDTH, HEIGHT = 500, 500
COLOURS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta"]


def get_number_of_racers():
    racers = 0

    while True:
        racers = input("How many racers (2-10)?\n> ")

        if racers.isdigit():
            racers = int(racers)
            
            if 2 <= racers <= 10:
                return racers
            else:
               print("Please enter a number between 2 and 10.")   
        
        else:
            print("Please enter a number.")

def race_turtles(colours):
    turtles = create_turtles(colours)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            _, y = racer.pos()
            if y >= (HEIGHT // 2) - 20:
                winner_index = turtles.index(racer)
                winner_colour = colours[winner_index]

                # Clear non-winners' pendowns
                for i, clear_racer_pendown in enumerate(turtles):
                    if i != winner_index:
                        clear_racer_pendown.clear()    
                
                # Clear non-winners' turtles
                for i, hide_racer in enumerate(turtles):
                    if i != winner_index:
                        hide_racer.hideturtle()   
            
                time.sleep(3)
                return winner_colour

def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")  

def create_turtles(colours):
    turtles = []
    spacing_x = WIDTH // (len(colours) + 1)
    for i, colour in enumerate(colours):
        x = -WIDTH // 2 + (i + 1) * spacing_x
        y = (-HEIGHT // 2) + 20

        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(x, y)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def get_colour_selection(colours):
    print("Colours playing this round:")
    for colour in colours:
        print(colour.capitalize(), end=". ")
    
    while True:
        selection = input("\nPlease select the colour you think will win: ").lower()
        if selection in colours:
            return selection
        else:
            print("Invalid input. Please enter a valid colour.")

racers = get_number_of_racers()


random.shuffle(COLOURS)
colours = COLOURS[:racers]
selection = get_colour_selection(colours)

print("Game running!")

init_screen()

winner = race_turtles(colours)

if winner == selection:
    print(f"Your selected colour {selection.upper()} has won!")
else:
    print(f"Sorry, your selected colour {selection.upper()} didn\'t win this time. {winner.upper()} won!")





