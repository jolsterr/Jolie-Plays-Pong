# Creating a pong game in Python 3
# By Jolie Fan

import turtle
import os

wn = turtle.Screen()
wn.title("Surprise Pong by @jolsterr")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player A - Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed (0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

# Player B - Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed (0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed (0)
ball.shape("square")
ball.color("grey")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Times New Roman", 24, "bold"))


# Function - Moving the pieces (Paddle Right)
def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

#Function - Moving the pieces (Paddle Left)
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

# Keyboard binding
wn.listen()
wn.onkey(paddle_right_up, "w")
wn.onkey(paddle_right_down, "s")
wn.onkey(paddle_left_up, "Up")
wn.onkey(paddle_left_down, "Down")

# Scoring
score_a = 0
score_b = 0

# Main Game Loop Time!
while True:
    wn.update()

    # Moving the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check (Top, Bottom, Left, Right)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bump2.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bump2.wav&")
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "bold"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "bold"))

# Collisions - Paddle and Ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bump2.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bump2.wav&")