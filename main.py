from turtle import Turtle, Screen
from ping import Ping
from ball import Ball
from score import Score
import time

window = Screen()
window.bgcolor("black")
window.setup(800, 600)
window.title("Pong Game")
window.tracer(0)

r_pong = Ping(350, 0)
l_pong = Ping(-350, 0)
ping = Ball()
scoreboardX = Score(-100, 255)
scoreboardY = Score(100, 255)

line = Turtle()
line.color("white")
line.hideturtle()
line.left(90)
line.forward(300)
line.backward(600)

window.listen()

window.onkey(r_pong.up, "Up")
window.onkey(r_pong.down, "Down")
window.onkey(l_pong.up, "w")
window.onkey(l_pong.down, "s")

gameIsOn = True

while gameIsOn:
    time.sleep(ping.move_speed)
    window.update()
    ping.move()

    if ping.ycor() > 280 or ping.ycor() < -280:
        ping.collision_updown()

    if ping.xcor() > 350:
        ping.game_over()
        scoreboardX.increase_scoreL()

    if ping.xcor() < -350:
        ping.game_over()
        scoreboardY.increase_scoreR()
    
    if ping.distance(r_pong) < 50 and ping.xcor() > 330:
        ping.collision_pong()

    if ping.distance(l_pong) < 50 and ping.xcor() < -330:
        ping.collision_pong()

window.exitonclick()