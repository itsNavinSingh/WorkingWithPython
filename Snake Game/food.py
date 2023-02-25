import turtle
import random
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(1, 1)
        self.color('blue')
        self.speed('fastest')
    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))