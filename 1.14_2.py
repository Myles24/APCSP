#   a114_make_it_start.py
#   Make the code draw 5 circles.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.goto(-150,5)
painter.shape("square")
painter.color("salmon")

line = 0 # This is the line you need to change.

while (line < 5): 
  painter.pendown()
  painter.circle(50)
  painter.penup()
  painter.forward(20)
  line = line + 1

wn = trtl.Screen()
wn.mainloop()