# learning Python by making a Pong game

import turtle

win = turtle.Screen()
win.title("Pong by Juan Mateo")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

player_one = turtle.Turtle()
player_one.speed(0) # animation speed max
player_one.shape("square")
player_one.color("white")
player_one.shapesize(stretch_wid=5, stretch_len=1) # default size 20x20
player_one.penup()
player_one.goto(-350, 0) # starting position

player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape("square")
player_two.color("white")
player_two.shapesize(stretch_wid=5, stretch_len=1)
player_two.penup()
player_two.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1 # play with these delta values. determines how much ball moves
ball.dy = 1

# functions to move player
def player_one_up():
  y = player_one.ycor()
  y += 20
  player_one.sety(y)

def player_one_down():
  y = player_one.ycor()
  y -= 20
  player_one.sety(y)

def player_two_up():
  y = player_two.ycor()
  y += 20
  player_two.sety(y)

def player_two_down():
  y = player_two.ycor()
  y -= 20
  player_two.sety(y)

# keyboard input
win.listen()
win.onkeypress(player_one_up, "w")
win.onkeypress(player_one_down, "s")
win.onkeypress(player_two_up, "Up")
win.onkeypress(player_two_down, "Down")


while True:
  win.update()

  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # borders

  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1

  # paddle able to bounce ball

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_one.ycor() + 40 and ball.ycor() > player_one.ycor() - 40):
    ball.setx(-340)
    ball.dx *= -1

  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_two.ycor() + 40 and ball.ycor() > player_two.ycor() - 40):
    ball.setx(340)
    ball.dx *= -1
