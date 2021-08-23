import turtle
turtle.bgcolor("black")
turtle.pensize(2.5)
turtle.speed(0.5)
color = ["violet","indigo","blue","green","yellow","orange","red"]
for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(130)
        turtle.left(10)
turtle.mainloop()