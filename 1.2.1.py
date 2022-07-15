import turtle as trtl
import random
import time
import leaderboard as lb

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle()

#-----game functions-----
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

delay = 0.1
 
pen = trtl.Turtle()
pen.penup()
pen.speed(0)
 
 
pen.goto(-100, 200)
 
score = 0
 
# black target circle
target = trtl.Turtle()
target.speed(0)
target.shape("circle")
target.color("black")
target.lt(90)
 

 
# writes the score on screen


def write():
    pen.clear()
    pen.write("Your score: " + str(score), font=("Calibri", 30, "bold"))
 
def clicked(x, y):
    global score
    score = score + 1
    target.penup()
    x = random.randint(-270, 290)
    y = random.randint(-270, 290)
    size = random.randint(1, 10)
    target.shapesize(size)
    target.goto(x, y)
    print(score)
    write()
    
def start_game():
    target.onclick(clicked)
    counter.getscreen().ontimer(countdown, counter_interval)
start_game()


    





wn = trtl.Screen()
wn.mainloop()
 
 
 

