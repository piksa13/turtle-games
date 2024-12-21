from turtle import  Turtle, Screen

jimmy = Turtle()

def move_forward():
    jimmy.forward(20)

def move_backward():
    jimmy.backward(20)

def turn_right():
    jimmy.right(10)

def turn_left():
    jimmy.left(10)

def clear_screen():
    jimmy.clear()
    jimmy.teleport(0,0, fill_gap=False)
#     or home() with penup()

screen = Screen()
screen.listen()
screen.onkeypress(fun=move_forward, key='w')
screen.onkeypress(fun=move_backward, key='s')
screen.onkeypress(fun=turn_right, key='a')
screen.onkeypress(fun=turn_left, key='d')
screen.onkeypress(fun=clear_screen, key='c')

screen.exitonclick()