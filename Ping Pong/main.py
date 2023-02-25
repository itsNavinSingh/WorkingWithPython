import turtle
import paddle
import random
import ball
gameon = True
def off():
    global gameon
    gameon = False
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(1000, 600)
screen.title('Pong')
cball = ball.Ball()
cball.setheading(random.randint(10, 80))
screen.tracer(0)
leftpaddle = paddle.Paddle((-480, 0))
rightpaddle = paddle.Paddle((480, 0))
rwrite = turtle.Turtle()
rwrite.color('white')
rwrite.penup()
rwrite.hideturtle()
rwrite.goto(-100, 290)
lwrite = turtle.Turtle()
lwrite.color('white')
lwrite.penup()
lwrite.hideturtle()
lwrite.goto(100, 290)
screen.listen()
screen.onkey(leftpaddle.moveup, 'w')
screen.onkey(leftpaddle.movedown, 's')
screen.onkey(rightpaddle.moveup, 'Up')
screen.onkey(rightpaddle.movedown, "Down")
screen.onkey(off, 'h')
while gameon:
    screen.update()
    cball.forward(1)
    if cball.ycor() < -280 or cball.ycor() > 280:
        cball.setheading(360-cball.heading())
    elif cball.xcor() > 500:
        leftpaddle.count += 1
        screen.tracer(0)
        cball.goto(0, 0)
        cball.setheading(random.randint(100, 170))
        screen.update()
    elif cball.xcor() < -500:
        rightpaddle.count += 1
        screen.tracer(0)
        cball.goto(0, 0)
        cball.setheading(random.randint(10, 80))
        screen.update()
    elif rightpaddle.distance(cball) < 30 and cball.xcor() > 470:
        cball.setheading(180-cball.heading())
    elif leftpaddle.distance(cball) < 30 and cball.xcor() < -470:
        cball.setheading(180-cball.heading())
    else:
        pass
    rwrite.write(f'Score:{rightpaddle.count}', align='center', font=('Courier', 80, 'normal'))
    lwrite.write(f'Score:{leftpaddle.count}', align='center', font=('Courier', 80, 'normal'))
    rwrite.clear()
    lwrite.clear()
screen.exitonclick()
print(leftpaddle.count)
print(rightpaddle.count)