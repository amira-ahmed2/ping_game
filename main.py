from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("my pang game")
screen.tracer(0)

ball = Ball()
score = Scoreboard()

paddle_r = Paddle(350, 0)
paddle_l = Paddle(-350, 0)

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320 ) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_potion()
        score.l_point()
        score.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset_potion()
        score.r_point()
        score.update_scoreboard()

















screen.exitonclick()