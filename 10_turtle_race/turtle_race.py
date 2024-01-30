import turtle, time

#CONSTS
WIDTH, HEIGHT = 500, 500

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

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")  

racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.left(90)
racer.backward(100)
time.sleep(5)

# https://youtu.be/NpmFbWO6HPU?si=007iG0goDm8u2mBe&t=13064