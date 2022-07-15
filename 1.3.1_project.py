import turtle as trtl
import keyboard
 
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
 
#-----countdown writer-----
counter =  trtl.Turtle()
 
# timer
def countdown():
  global timer
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
   
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
 
delay = 0.1
 
# initialize score writer
pen = trtl.Turtle()
pen.penup()
pen.speed(0)
pen.goto(-100, 200)
 
score = 0
 
# black target circle
target = trtl.Turtle()
target.penup()
target.goto(-600, 350)
target.speed(0)
target.shape("circle")
target.color("black")
 
# bullet turtle
bullet = trtl.Turtle()
bullet.speed(0)
bullet.shape("square")
bullet.color("blue")
bullet.shapesize(.2)
bullet.lt(90)
bullet.penup()
 
# spike turtle
b_turt = trtl.Turtle()
b_turt.penup()
b_turt.speed(0)
b_turt.shape("triangle")
b_turt.color("red")
b_turt.goto(0, -350)
b_turt.lt(90)
 
# writes the score on screen
def write():
    pen.clear()
    pen.write("Your score: " + str(score), font=("Calibri", 30, "bold"))
 
# function that moves bullet with spike
def follow():
    bullet.goto(b_turt.xcor(), b_turt.ycor())
   
# target movement variables
sides = 500
forward2 = 10
 
while True:
    # if Enter is pressed, the game starts
    if keyboard.is_pressed('Enter'):
        target.speed(1)
        target.penup()
        print(target.pos)
        countdown()
 
 
        while True:
            if timer <= 0:
                break
           
            print(target.pos())
           
            # moves target back and forth on screen
            target.forward(forward2)
            if target.xcor() >= 500:
                x = target.xcor() - 10
                forward2 = -10
            elif target.xcor() <= -500:
                x = target.xcor() + 10
                forward2 = 10
 
            # mapping shoot key
            if keyboard.is_pressed("Up"):
                bullet.forward(711.5)
 
                # hit detection
                if bullet.ycor() - 25 <= target.ycor() <= bullet.ycor() + 25 and bullet.xcor() - 25 <= target.xcor() <= bullet.xcor() + 25:
                    score = score + 1
                    write()
                else:
                    pass
               
            # mapping directional keys
            if keyboard.is_pressed("Right"):
                right = b_turt.xcor() + 5
                b_turt.goto(right, -350)
                follow()
            if keyboard.is_pressed("Left"):
                left = b_turt.xcor() - 5
                b_turt.goto(left, -350)
                follow()
 
            # mapping Ctrl to control faster movement    
            if keyboard.is_pressed("Ctrl"):
                if keyboard.is_pressed("Right"):
                    right = b_turt.xcor() + 30
                    b_turt.goto(right, -350)
                    follow()
                if keyboard.is_pressed("Left"):
                   
                    left = b_turt.xcor() - 30
                    b_turt.goto(left, -350)
                    follow()
 
            # allows another attempt in the loop
            if keyboard.is_pressed('Enter'):
                target.forward(10)
                target.color("black")
                target.penup()
                print(target.pos)
               
wn = trtl.Screen()
wn.mainloop()
 
 
 
 
 
 
 
 
 
 
 
 
 
 

