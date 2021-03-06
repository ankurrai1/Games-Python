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

def draw_fig(x,y,shape,color,isPaddle = True):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape(shape)
    paddle.color(color)
    if isPaddle:
        paddle.shapesize(stretch_wid = 5, stretch_len = 1)
    paddle.penup()
    paddle.goto(x,y)
    return paddle

paddle_a = draw_fig(-350,0,"square","white")
paddle_b = draw_fig(350,0,"square","white")
ball = draw_fig(0,0,"square","white",False)


def getpen_to():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    return pen


def update_score(pen,A,B):
    pen.clear()
    pen.write("player A:{} player B: {}".format(A,B),align="center",font=("Arial",15, "normal"))


# this two will define the speed of ball move
ball.dx = 5
ball.dy = - 5


def move_paddel(paddle,direction,movement = 20):
    y = paddle.ycor()
    if direction == "up":
            y +=20
    else if direction == "down":
        y -=20
    paddle.sety(y)

#keyboard Bindings
window.listen()
window.onkeypress(move_paddel(paddle_a,"up"),"w")
window.onkeypress(move_paddel(paddle_a,"down"),"s")
window.onkeypress(move_paddel(paddle_b,"up"),"Up")
window.onkeypress(move_paddel(paddle_b,"down"),"Down")

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
        update_score(score_a,score_b)

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dy *=-1
        score_b += 1
        update_score(score_a,score_b)

    # paddle ball collision detection
    if ( ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx*=-1
        os.system("afplay pong.wav&")

    if ( ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx*=-1
        os.system("afplay pong.wav&")
