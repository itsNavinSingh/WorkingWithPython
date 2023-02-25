import turtle
class Paddle(turtle.Turtle):
    count = 0
    def __init__(self, cordinate):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.goto(cordinate)
    def moveup(self):
        self.forward(80)
    def movedown(self):
        self.backward(80)
