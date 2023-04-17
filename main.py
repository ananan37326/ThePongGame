import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from boundary import Boundary
import time

# Screen
screen = t.Screen()
screen.setup(width=840, height=700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddleRight = Paddle((380,0),"red")
paddleLeft = Paddle((-390,0),"blue")
ball = Ball()
score = Scoreboard()
boundary = Boundary()

screen.listen()
screen.onkeypress(paddleRight.up, "Up")
screen.onkeypress(paddleRight.down,"Down")

screen.onkeypress(paddleLeft.up,"w")
screen.onkeypress(paddleLeft.down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddleRight) < 50 and ball.xcor() > 350 or ball.distance(paddleLeft) < 50 and ball.xcor() < -360:
        ball.bounce_x()
        ball.increase_speed()


    # detect when the right paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.update_l_score()

    # detect when the left paddle misses the ball
    if ball.xcor() < -390:
        ball.reset_position()
        score.update_r_score()

    if score.reached_max_score():
        game_is_on = False
        score.game_over()

screen.exitonclick()