from random import random
from turtle import  Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_init_position = -100
is_race_on = False
all_turtles = []

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle win the race? Enter color: ')

for turtle_number in range(6):
     new_turtle = Turtle('turtle')
     new_turtle.penup()
     new_turtle.goto(x =-230, y=y_init_position)
     y_init_position = y_init_position + 40
     new_turtle.color(colors[turtle_number])
     all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            if turtle.pencolor() == user_bet:
                print(f'Your {turtle.pencolor()} turtle won the game! Good bet.')
            else:
                print(f'Your bet was wrong, {turtle.pencolor()} won the race.')
            is_race_on = False







screen.exitonclick()