import turtle
import random
screen = turtle.Screen()
Uinp = screen.textinput('Make Your bet', 'Which turtle will win the race? Enter the color: ')
screen.setup(500, 400)
colorlist = ['red', 'green', 'blue', 'yellow', 'black']
turtules = []
for c in range (5):
    point = turtle.Turtle()
    point.penup()
    point.color(colorlist[c])
    point.goto(-200, -175+c*75)
    turtules.append(point)
race_on = False
if Uinp:
    race_on = True
while race_on:
    for turt in turtules:
        if turt.xcor() > 230:
            race_on = False
            colo = turt.pencolor()
            break
        turt.forward(random.randint(1,25))
if colo == Uinp:
    print('WOW! You guessed it right!')
else:
    print('OPPs! Wrong guessed')
print(f'{colo} coloured turtle win the race.')
screen.exitonclick()