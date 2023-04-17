from turtle import Turtle

# class for bounding box creating a 800*600 boundary for the game
class Boundary:
    def __init__(self):
       self.up = Turtle()
       self.down = Turtle()
       self.left = Turtle()
       self.right = Turtle()
       self.create_boundary()

    def initialize_turtle(self, turtle, w, l):
        turtle.shape("square")
        turtle.color("white")
        turtle.shapesize(stretch_wid=w, stretch_len=l)
        turtle.penup()

    def create_boundary(self):
        self.initialize_turtle(self.up,0.5,40)
        self.initialize_turtle(self.down,0.5,40)
        self.initialize_turtle(self.left, 30.5, 0.5)
        self.initialize_turtle(self.right, 30.5, 0.5)

        self.up.goto(0,300)
        self.down.goto(0,-300)
        self.left.goto(-405,0)
        self.right.goto(395,0)
