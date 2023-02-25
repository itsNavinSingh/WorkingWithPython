import turtle
class Scoreboard(turtle.Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        with open('bestscore.txt') as bestscore:
            self.highscore = int(bestscore.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.updatescoreboard()
    def scoreadd(self):
        self.score += 1
    def updatescoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', align='center', font=('Arial', 15, 'normal'))
    def clearescore(self):
        self.updatescoreboard()
    def resetscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("bestscore.txt", mode='w') as rewrite:
                rewrite.write(str(self.highscore))
        self.score = 0