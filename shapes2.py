from turtle import *

sides = int(input("Enter number of sides:"))
angle = 360/sides

color1 = input("Enter border color:")
color2 = input("Fill Color? Yes/No:")
if color2 == "Yes":
    fillcolor=True
    color3 = input("Enter fill color:")
    sidelength = int(input("Enter length of the side:"))
else:
    fillcolor=False
    sidelength = int(input("Enter length of the side:"))

print ("sides:", sides, "angle:", angle)
setup(500, 500)
penup()
setposition(0, 200)
pendown()
pencolor(color1)

if fillcolor == True:
    fillcolor=color3
    begin_fill()
    for draw in range(sides):
        forward(sidelength)
        right(angle)
        forward(sidelength)
    end_fill()
else:
    for draw in range(sides):
        forward(sidelength)
        right(angle)
        forward(sidelength)

exitonclick()
