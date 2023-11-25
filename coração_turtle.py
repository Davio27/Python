import turtle

def coracao():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.setheading(60)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

coracao()
turtle.done()