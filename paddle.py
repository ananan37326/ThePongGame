from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position,color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color(color)
        self.penup()
        x,y = position
        self.goto(x,y)

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        if y > 245:
            y = 245
        self.goto(x,y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        if y < -245:
            y = -245
        self.goto(x, y)


