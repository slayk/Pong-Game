from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        incX = self.xcor() + self.x_move
        incY = self.ycor() + self.y_move
        self.goto(incX, incY)
    
    def collision_updown(self):
        self.y_move *= -1
    
    def collision_pong(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def game_over(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.collision_pong()