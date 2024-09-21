import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("The Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 350 :
        ball.new_game()
        score.l_point()

    if ball.xcor() < -350:
        ball.new_game()
        score.r_point()

screen.exitonclick()
