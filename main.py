import turtle as t
import random

asghar = t.Turtle()
t.colormode(255)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

asghar.width(10)
asghar.speed(0)
asghar.teleport(x=-250, y=-250)


for _ in range(90):
    y_side = asghar.ycor()
    asghar.pencolor(random.choice(color_list))
    asghar.dot()
    asghar.penup()
    asghar.forward(50)
    asghar.dot()
    if asghar.xcor() == 200:
        asghar.teleport(x=-250, y=y_side+50)




screen = t.Screen()
screen.exitonclick()

