#   a115_robot_maze.py
import turtle as trtl
import keyboard


#----- maze and turtle config variables


screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()



#---- TODO: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

#p = robot.pos()
#robot.write(str(p), True)


while True:
  print(robot.pos())
  wn.listen()
  if keyboard.is_pressed('Right'):
    robot.rt(90)
    robot.fd(50) 
    robot.lt(90)
  elif keyboard.is_pressed('Up'):
    robot.fd(50)
  elif keyboard.is_pressed('Left'):
    robot.lt(90)
    robot.fd(50) 
    robot.rt(90)
  elif keyboard.is_pressed('Down'):
    robot.backward(50)
  elif keyboard.is_pressed('r'):
    break
  else:
    pass

  win = 0

  if robot.pos() == (100, 0):
    robot.goto(-100, -100)
  elif robot.pos() == (100, -50):
    robot.goto(-100, -100)
  elif robot.pos() == (0, -100):
    robot.goto(-100, -100)
  elif robot.pos() == (-100, 0):
    robot.goto(-100, -100)
  elif robot.pos() == (-50, 100):
    robot.goto(-100, -100)
  elif robot.pos() == (0, 100):
    robot.goto(-100, -100)
  elif robot.pos() == (50, -100):
    robot.goto(-100, -100)
  elif robot.pos() == (0, 100):
    robot.goto(-100, -100)
  if robot.pos() == (0, 0):
    win = win + 1
  elif robot.pos() == (100, 100):
    win = win + 1
  if win == 2:
    print("you win, LIBTARD")



  
  

   





  





#---- end robot movement 

wn.mainloop()
