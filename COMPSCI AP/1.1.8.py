#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import time


# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]


# assigns this for statement as variable s and runs through each color assigning it a different turtle and appending it to horiz_turtles and moves turtle 50 more than the last coord
tloc = 50
for s in turtle_shapes:

# assigns turtle the variable ht 
  ht = trtl.Turtle(shape=s)
  # appends the turtle ht to horiz_turtles
  horiz_turtles.append(ht)
  ht.penup()

  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions


steps = 0
pixel_size = 20
distance = 3
while steps < 50:
  steps = steps + 1

  for ht in horiz_turtles:
    for vt in vert_turtles:
      ht.forward(distance)
      vt.forward(distance)
  
    if abs(ht.xcor() - vt.xcor()) < pixel_size:
      if abs(ht.ycor()) - vt.ycor() < pixel_size:
        ht.fillcolor("gray")
        horiz_turtles.remove(ht)
        vt.fillcolor("gray")
        vert_turtles.remove(vt)


wn = trtl.Screen()
wn.mainloop()