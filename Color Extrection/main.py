import turtle
import random
import colorgram

colors = colorgram.extract('img.jpg', 10)
Color_Patern = []
for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    Color_Patern.append((red, green, blue))

screen = turtle.Screen()
Point = turtle.Turtle()
turtle.colormode(255)
Point.setheading(200)
Point.penup()
Point.forward(450)
Point.setheading(0)
for i in range(15):
    for j in range(25):
        Point.dot(10, random.choice(Color_Patern))
        Point.forward(30)
    Point.backward(30*25)
    Point.left(90)
    Point.forward(30)
    Point.right(90)


screen.exitonclick()