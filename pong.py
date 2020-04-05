# Simple pong game in python 3
# this game is based on turtle

import turtle

Width = 800
Height = 600

#Window setup
window = turtle.Screen()
window.title("Pong Game By ankurrai1")
window.bgcolor("black")
window.setup(width = Width, height = Height)
window.tracer(1)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0 player B: 0",align="center",font=("Arial",12, "normal"))

# this two will define the speed of ball move
ball.dx = 5
ball.dy = - 5

def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#keyboard Bindings
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

while True:
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # top bottom boder checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *=-1

    # left right boder checking
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dy *=-1

    # paddle ball collision detection
    if ( ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx*=-1

    if ( ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx*=-1
