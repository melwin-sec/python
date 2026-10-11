
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)
pen.color("white", "red")

pen.begin_fill()

pen.left(140)
pen.forward(150)
pen.circle(-75, 200)
pen.left(120)
pen.circle(-75, 200)
pen.forward(150)

pen.end_fill()

pen.hideturtle()
turtle.done()
