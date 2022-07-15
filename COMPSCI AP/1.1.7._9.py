#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl


# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)
  t.color(turtle_colors.pop())

direction = 90
forward = 50


#  
startx = 0
starty = 0

#
for t in my_turtles:
    t.goto(startx, starty)
    t.pendown()
    t.setheading(direction) 
    t.right(45)    
    t.forward(forward)
  


#	
    startx = t.xcor()
    starty = t.ycor()
    direction = t.heading()
    forward += 3

wn = trtl.Screen()
wn.mainloop()