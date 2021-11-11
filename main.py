import turtle as trtl

# Setup Variables
numSides = 25
length = 20
doorSize = 40
wallPiece = 5
# Turtle Settings
painter = trtl.Turtle()
painter.speed("fastest")
painter.pensize(5)

currentSide = 0
currentSize = length
while (currentSide < numSides):
    if (currentSide < 4):
        painter.forward(currentSize)
        painter.left(90)

    else:
        painter.forward(wallPiece)
        painter.penup()
        painter.forward(doorSize)
        painter.pendown()
        painter.left(90)
        painter.forward(length)
        painter.right(180)
        painter.forward(length)
        painter.left(90)
        painter.forward(currentSize - doorSize - wallPiece)

    painter.left(90)
    currentSize += length
    currentSide+=1


painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
