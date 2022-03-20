from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong.io")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

ball = Ball()
score = Scoreboard()
screen.listen()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.change_speed)
    screen.update()
    ball.move()

    #Detect collisions with top and bottom walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Bounce the ball
        ball.bounce_y()

    #Detect collision with both paddles.
    if ball.distance(r_paddle) < 30 and ball.xcor() > 320 or ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect when right paddle misses the ball.
    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_points()

    #Detect when right paddle misses the ball.
    if ball.xcor() < -380 :
        ball.reset_position()
        score.r_points()

screen.exitonclick()