from turtle import*
fillcolor('#F6D02F')
begin_fill()
pensize(5)
penup()
circle(130, 40)
pendown()
circle(100, 105)
left(180)
circle(-100, 5)
seth(20)
circle(300, 30)
circle(30, 50)
seth(190)
circle(300, 36)
seth(150)
circle(150, 70)
seth(200)
circle(300, 40)
circle(30, 50)
seth(20)
circle(300, 35)
seth(240)
circle(105, 95)
left(180)
circle(-105, 5)
seth(210)
circle(500, 18)
seth(200)
fd(10)
seth(280)
fd(7)
seth(210)
fd(10)
seth(300)
circle(10, 80)
seth(220)
fd(10)
seth(300)


fillcolor('#000000')
begin_fill()
pensize(5)
seth(330)
circle(100, 35)
seth(219)
circle(-300, 19)
seth(110)
circle(-30, 50)
circle(-300, 10)
end_fill()

fillcolor('#000000')
begin_fill()
pensize(5)
seth(300)
circle(-100, 30)
seth(35)
circle(300, 15)
circle(30, 50)
seth(190)
circle(300, 17)
end_fill()

seth(60)
fillcolor('#DD4D28')
begin_fill()
a = 2.3
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
        lt(3)
        fd(a)
    else:
        a += 0.05
        lt(3)
        fd(a)
        end_fill()
        turtles