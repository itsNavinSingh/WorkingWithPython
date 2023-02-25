import turtle
import time
import snake
import food
import scoreboard
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
score = scoreboard.Scoreboard()
screen.title('My Snake Game')
screen.tracer(0)
sanake = snake.Snake()
Food = food.Food()
screen.listen()
screen.onkey(sanake.up, 'Up')
screen.onkey(sanake.down, 'Down')
screen.onkey(sanake.left, 'Left') 
screen.onkey(sanake.right, 'Right')
game_is_on = True
def gameoff():
    global game_is_on
    game_is_on = False
screen.onkey(gameoff, 'x')
while game_is_on:
    screen.update()
    time.sleep(0.2)
    sanake.move()
    score.clearescore()
    if sanake.segments[0].distance(Food) < 15:
        Food.refresh()
        sanake.add_snake()
        score.scoreadd()
    score.updatescoreboard
    for pos in range (1, len(sanake.segments)):
        if sanake.segments[0].distance(sanake.segments[pos]) < 15:
            score.resetscore()
            sanake.resetsnake()
            break
    if sanake.segments[0].xcor() > 300 or sanake.segments[0].xcor() < -300 or sanake.segments[0].ycor() > 300 or sanake.segments[0].ycor() < -300:
        score.resetscore()
        sanake.resetsnake()

baba = turtle.Turtle()
baba.color('white')
baba.hideturtle()
baba.write(f'Game Over!', align='center', font=('Arial', 15, 'normal'))
screen.exitonclick()

