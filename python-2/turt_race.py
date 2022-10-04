import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle do you think will win? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_on = False
all_turtles = []
y = -120


for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.pu()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y)
    all_turtles.append(tim)
    y += 40

if user_bet:
    race_on = True

while race_on:
    for runner in all_turtles:
        random_distance = random.randint(0, 10)
        runner.forward(random_distance)
        if runner.xcor() > 230:
            if runner.pencolor() == user_bet:
                print(f"{user_bet} was the right bet! Congrats :)")
            else:
                print(f"{runner.pencolor()} has won the race...better luck next time :)")
            race_on = False




screen.exitonclick()