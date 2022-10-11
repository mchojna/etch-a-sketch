import turtle
import random


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def move_left():
    tom.left(10)


def move_right():
    tom.right(10)


def reset():
    turtle.resetscreen()


def color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tom.pencolor((r, g, b))


def up_down():
    global n
    if n % 2 == 0:
        tom.penup()
    else:
        tom.pendown()
    n += 1


tom = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()

n = 0

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="r", fun=reset)
screen.onkey(key="c", fun=color)
screen.onkey(key="space", fun=up_down)

screen.exitonclick()
