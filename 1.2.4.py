import turtle as trtl
import random as rand

#configuration
walls = trtl.Turtle()
walls.speed(0)
wallLength = 0 
pathWidth = 30 
doorWidth = 25 

mazeRunner = trtl.Turtle(shape="square")
mazeRunner.turtlesize(0.3)

mazeRunner.color("blue")
mazeRunner.pencolor("red")
mazeRunner.hideturtle()

#functions
def drawBarrier(pathW):
  walls.left(90)
  walls.forward(pathW)
  walls.forward(-pathW)
  walls.right(90)

def drawDoor(doorW):
  walls.pu()
  walls.forward(doorW)
  walls.pd()

def moveRunner():
  mazeRunner.forward(5)

def runnerUp():
  mazeRunner.setheading(90)

def runnerLeft():
  mazeRunner.setheading(180)

def runnerRight():
  mazeRunner.setheading(0)

def runnerDown():
  mazeRunner.setheading(270)



#Do stuff here

#build the wall
for i in range(25):
  walls.left(90)
  
  #add doors and barriers
  if i > 6:
    doorSpot = rand.randint(0,10+wallLength-doorWidth)
    barrierSpot = rand.randint(0,10+wallLength-doorWidth)
    
    while barrierSpot > doorSpot and barrierSpot < (doorSpot+doorWidth):
        barrierSpot = rand.randint(0,10+wallLength-doorWidth)
    if barrierSpot <= doorSpot:
      walls.forward(barrierSpot) 
      drawBarrier(pathWidth)
      walls.forward(doorSpot-barrierSpot) 
      drawDoor(doorWidth)
      walls.forward(10+wallLength-doorWidth-doorSpot)
    else: 
      walls.forward(doorSpot) 
      drawDoor(doorWidth)
      walls.forward(barrierSpot-doorSpot) 
      drawBarrier(pathWidth)
      walls.forward(10+wallLength-doorWidth-barrierSpot)
 
  elif i > 1: 
    doorSpot = rand.randint(0,10+wallLength-doorWidth)
    walls.forward(doorSpot) 
    drawDoor(doorWidth)
    walls.forward(10+wallLength-doorWidth-doorSpot)
  
  else:
    walls.forward(10) 
    walls.forward(wallLength)
  wallLength +=15

walls.hideturtle()

mazeRunner.showturtle()



wn = trtl.Screen()

wn.onkeypress(runnerUp, 'w')
wn.onkeypress(runnerLeft, 'a')
wn.onkeypress(runnerDown, 's')

wn.listen()
wn.mainloop()