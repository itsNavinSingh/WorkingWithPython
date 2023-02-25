import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_score()
    def increase_level(self):
        self.Level += 1
        self.clear()
        self.update_score()
    def update_score(self):
        self.write(f'Level:{self.Level}', align='left', font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=FONT)
