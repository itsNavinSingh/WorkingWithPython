import turtle
import pandas
screen = turtle.Screen()
screen.title('States of INDIA')
turtle.addshape('indstates.gif')
turtle.shape('indstates.gif')
data = pandas.read_csv('Stateslist.csv')
allState = data.State.to_list()
Correct = 0
answer = 'baba'
answeredlist = []
while Correct < 28 and answer.lower() != 'exit':
    answer = screen.textinput(title=f'Score: {Correct}/28', prompt='Guess next states')
    if answer.upper() in answeredlist:
        pass
    else:
        if answer.lower() in allState:
            answeredlist.append(answer.upper())
            Correct += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.State == answer.lower()]
            t.goto(int(state_data.X), int(state_data.Y))
            t.write(answer.title())
missedstate = []
if Correct != 28:
    for leftstate in allState:
        if leftstate.upper() not in answeredlist:
            missedstate.append(leftstate.title())
for sateoff in missedstate:
    screen.tracer(0)
    p = turtle.Turtle()
    p.hideturtle()
    screen.update()
    p.penup()
    p.color('red')
    misseddata = data[data.State == sateoff.lower()]
    p.goto(int(misseddata.X), int(misseddata.Y))
    p.write(sateoff)
screen.exitonclick()
