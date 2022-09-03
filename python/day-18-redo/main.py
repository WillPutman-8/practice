import turtle as t
import random
timy = t.Turtle()
timy.speed("fastest")
timy.shape("turtle")
t.colormode(255)

def rando_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(360):
    timy.circle(100)
    timy.color(rando_color())
    current_heading = timy.heading()
    timy.setheading(current_heading + 1)



screen = t.Screen()
screen.exitonclick()

















screen = Screen()
screen.exitonclick()