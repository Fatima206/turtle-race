from turtle import Turtle, Screen
import random
from tkinter import messagebox

is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    # list of multiple turtle instances that each have a different state

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                messagebox.showinfo(title="Result", message=f"You won! The {winning_color} turtle is the winner!")
                # print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                messagebox.showinfo(title="Result", message=f"You lost! The {winning_color} turtle is the winner!")
                # print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
