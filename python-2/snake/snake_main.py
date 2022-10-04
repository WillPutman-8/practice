from turtle import Screen
from snake2 import Snake
import time

# setting up the screen for the snake game.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()

game_on = True
while game_on:
    snake.move()

screen.exitonclick()
