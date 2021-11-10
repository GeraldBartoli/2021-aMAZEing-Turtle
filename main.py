import turtle as trtl

maze = trtl.Turtle()

maxloopside = 25
a = 0
length = 10

maze.left(90)

while (a < maxloopside):
    maze.forward(50)
    maze.right(90)


wn = trtl.Screen()
wn.mainloop()
