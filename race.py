import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet= screen.textinput(title ="Make your bet", prompt= " Which turtle will win the race ? Enter a color = ")
color_turtle = ["red","blue","yellow","orange","black",'green']
y_position =[ -78,-48, -18, 20,50,80]
all_turtle = []
for turtle_index in range(0,6):

    tin = Turtle(shape="turtle")
    tin.color(color_turtle[turtle_index])
    tin.penup()
    tin.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(tin)
if user_bet:
    is_race_on = True
    while is_race_on:

        for turtle in all_turtle:
         if turtle.xcor()>230:

             is_race_on = False
             winning_color = turtle.pencolor()
             if winning_color == user_bet:
                 print(f"You have won !  The {winning_color}  turtle is the winner !")
             else:
                 print(f"You have lost! the {winning_color} turtle is the winner !")

         random_distance = random.randint(0,10)
         turtle.forward(random_distance)


screen.exitonclick()