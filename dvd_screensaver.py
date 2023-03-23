import turtle
import random

#
# So this is a DVD Screensaver emulator using Turtle Graphics.
# It hits the corner sometimes.
# Not util at all, but its fun.
#
# Version: 2
#
# CC 2022 EM Gavela
#


# List of colors.
colors = ["green","blue","red","white","orange","yellow","pink"]

# Window Setup

window = turtle.Screen()
window.title("DVD Screensaver")
window.setup(width = 800,height = 600)
window.bgcolor("black")
window.tracer(0)

# Block setup.

block = turtle.Turtle()
block.speed(0)
block.shape("square")
block.color("white")
block.shapesize(stretch_wid = 5,stretch_len = 6)
block.penup()
block.goto(0,0)

# Speed? Depends on the processor.

block.dx = 0.06
block.dy = -0.06

#Main game loop

while True:

    window.update()

    #Movement of the block.

    block.setx(block.xcor() + block.dx)
    block.sety(block.ycor() + block.dy)

    # Collisions: What happens when the block touches a border.

    if block.ycor() > 250:
        block.sety(250)
        block.dy *= -1 #Change direction
        block.color(colors[random.randint(0,len(colors)) - 1])

    if block.ycor() < -250:
        block.sety(-250)
        block.dy *= -1
        block.color(colors[random.randint(0,len(colors))-1])

    if (block.xcor() < -340 and block.xcor() > -350):
        block.dx *= -1
        block.color(colors[random.randint(0,len(colors))-1])

    if (block.xcor() > 340 and block.xcor() < 350):
        block.dx *= -1
        block.color(colors[random.randint(0,len(colors))-1])
