# first Game Pong by Agrisimo 22/01/2021

import turtle
import time
import winsound

win = turtle.Screen()
win.title("Pong game by Agrisimo")
win.bgcolor("blue")
# 0,0 coordiantes are in centre!
win.setup(width=800, height=600)
win.tracer(0)

#Player A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
#standard size is 20x20 pixels. It`s stretched by multiplyer of:
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-390,0)

#Player B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
#standard size is 20x20 pixels. It`s stretched by multiplyer of:
paddle_b.shapesize(stretch_wid=5, stretch_len=-1)
paddle_b.penup()
paddle_b.goto(+380,10)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
#standard size is 20x20 pixels. It`s stretched by multiplyer of:
ball.penup()
ball.goto(+0,0)

#Ball movement
ball.deltax = 0.2
ball.deltay = 0.2

#Pen scoring
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player Green = {score_a}   {score_b} = Player Red", align="center", font=("Courier", 24, "normal"))

#Movement functions paddle a

def up_a():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def down_a():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
#Movement functions paddle b
def up_b():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def down_b():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
win.listen()
win.onkeypress(up_a, "w")
win.onkeypress(down_a, "s")

win.onkeypress(up_b, "Up")
win.onkeypress(down_b, "Down")

#Main game loop
while True:
    win.update()
    # move the ball
    ball.setx(ball.xcor() + ball.deltax)
    ball.sety(ball.ycor() + ball.deltay)
    #Border cheking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.deltay = ball.deltay *-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.deltay = ball.deltay *-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0,0)
        print("Green player scored!")
        time.sleep(1)
        ball.deltax = ball.deltax *-1
        score_a += 1
        pen.clear()
        pen.write(f"Player Green = {score_a}   {score_b} = Player Red", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        print("Red player scored!")
        time.sleep(1)
        ball.deltax = ball.deltax * -1
        score_b += 1
        pen.clear()
        pen.write(f"Player Green = {score_a}   {score_b} = Player Red", align="center", font=("Courier", 24, "normal"))

    # Collisions
    if ball.xcor() > 360 and ball.xcor() < 370 and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60:
        ball.setx(360)
        ball.deltax *= -1
        ball.deltax *= 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -368 and ball.xcor() > -378 and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60:
        ball.setx(-368)
        ball.deltax *= -1
        ball.deltax *= 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)