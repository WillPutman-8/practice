import random
import turtle
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.penup()
timmy.shape("turtle")
timmy.setposition(-400, -300)
rgb_colors = [
 (243, 234, 76), (211, 158, 93), (188, 12, 69),
 (111, 179, 208), (25, 116, 169), (172, 172, 31),
 (221, 128, 166), (160, 78, 35), (128, 186, 146), (10, 32, 76),
 (235, 73, 41), (31, 135, 83), (176, 48, 95), (234, 165, 194),
 (79, 13, 63), (12, 55, 34), (236, 228, 6), (29, 164, 207), (15, 42, 132), (58, 165, 95)]

def turtle_dot():
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

def turtle_left():
    timmy.left(90)
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)
    timmy.left(90)

def turtle_right():
    timmy.right(90)
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)
    timmy.right(90)

def turtle_run():
    for _ in range(10):
        turtle_dot()
    turtle_left()

    for _ in range(10):
        turtle_dot()
    turtle_right()


for _ in range(5):
    turtle_run()

screen = turtle.Screen()
screen.exitonclick()
