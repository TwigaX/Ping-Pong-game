from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.goto(0,0)

    def move(self):
        #self.setheading(45)
        new_x = self.xcor() +10
        new_y = self.ycor() +10
        self.goto(new_x, new_y)
