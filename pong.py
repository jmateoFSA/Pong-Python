#learning Python by making a Pong game

import turtle

win = turtle.Screen()
win.title("Pong by Juan Mateo")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

player_one = turtle.Turtle()
player_one.speed(0) #animation speed max
player_one.shape("square")
player_one.color("white")
player_one.shapesize(stretch_wid=5, stretch_len=1) #default size 20x20
player_one.penup()
player_one.goto(350, 0) #starting position

player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape("square")
player_two.color("white")
player_two.shapesize(stretch_wid=5, stretch_len=1)
player_two.penup()
player_two.goto(-350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

while True:
  win.update()
