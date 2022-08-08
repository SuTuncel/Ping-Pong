from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.color("purple")
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
