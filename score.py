from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.current_scoreL = 0
        self.current_scoreR = 0
        self.update_scoreL()
        self.update_scoreR()
        
    def update_scoreL(self):
        self.write(f"{self.current_scoreL}", move=False, align="left", font=("Arial", 25, "normal"))

    def update_scoreR(self):
        self.write(f"{self.current_scoreR}", move=False, align="left", font=("Arial", 25, "normal"))

    def increase_scoreL(self):
        self.clear()
        self.current_scoreL += 1
        self.update_scoreL()

    def increase_scoreR(self):
        self.clear()
        self.current_scoreR += 1
        self.update_scoreR()