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

while True:
    window.update()
