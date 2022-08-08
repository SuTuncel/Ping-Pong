from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
 # Screen
screen = Screen()
screen.title("PINK PONG GAME")
screen.setup(width=800, height=600)
screen.bgcolor("pink")
screen.tracer(0)
 #Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboardd = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #collision with the ball
    if ball.ycor() > 290 or ball.ycor() < -290:
        # needs bounds
        ball.bounce_y()

    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) and ball.xcor() < -320:
        ball.bounce_x()

    #detect a r paddle misses
    if ball.xcor() > 300:
        ball.reset_position()
        scoreboardd.l_point()

    #detect a l paddle misses
    if ball.xcor() < -300:
        ball.reset_position()
        scoreboardd.r_point()


screen.exitonclick()
