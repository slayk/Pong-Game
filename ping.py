from turtle import Turtle

class Ping(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)

    def up(self):
        newY = self.ycor() + 40
        self.goto(self.xcor(), newY)

    def down(self):
        newY = self.ycor() - 40
        self.goto(self.xcor(), newY)