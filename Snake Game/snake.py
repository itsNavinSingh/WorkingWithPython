import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = turtle.Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def add_snake(self):
        new_segment = turtle.Turtle(shape='square')
        lastpiece = self.segments[len(self.segments) - 1]
        lastx = lastpiece.xcor()
        lasty = lastpiece.ycor()
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(lastx, lasty)
        self.segments.append(new_segment)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def resetsnake(self):
        for snake in self.segments[4:]:
            self.segments.remove(snake)
            snake.hideturtle()
        self.segments[0].goto(0, 0)
