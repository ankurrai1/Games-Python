# Simple pong game in python 3
# this game is based on turtle

import turtle
import os

Width = 800
Height = 600
score_a = 0
score_b = 0

#Window setup
window = turtle.Screen()
window.title("Pong Game By ankurrai1")
window.bgcolor("black")
window.setup(width = Width, height = Height)
window.tracer(1)

def draw_fig(x,y,shape,color,shapfact = True):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape(shape)
    paddle.color(color)
    if shapfact:
        paddle.shapesize(stretch_wid = 5, stretch_len = 1)
    paddle.penup()
    paddle.goto(x,y)

draw_fig(-350,0,"square","white")
draw_fig(350,0,"square","white")
draw_fig(0,0,"square","white")


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A: 0 player B: 0",align="center",font=("Arial",15, "normal"))

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
        os.system("afplay pong.wav&")

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *=-1
        os.system("afplay pong.wav&")

    # left right boder checking
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("player A:{} player B: {}".format(score_a,score_b),align="center",font=("Arial",15, "normal"))

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dy *=-1
        score_b += 1
        pen.clear()
        pen.write("player A:{} player B: {}".format(score_a,score_b),align="center",font=("Arial",15, "normal"))

    # paddle ball collision detection
    if ( ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx*=-1
        os.system("afplay pong.wav&")

    if ( ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx*=-1
        os.system("afplay pong.wav&")
