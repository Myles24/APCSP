import turtle as trtl
import random
import keyboard
 
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
 
 
 
while True:
    # if Enter is pressed, the black circle will go to random coor
    if keyboard.is_pressed('Enter'):
        target.penup()
        x = random.randint(-270, 290)
        y = random.randint(-270, 290)
        target.goto(x, y)
        print(target.pos)
        while True:
            # mapping keys to turn turtle
            target.speed(100)
            target.backward(10)
            if keyboard.is_pressed("Right"):
                right = b_turt.xcor() + 5
                b_turt.goto(right, -350)
            if keyboard.is_pressed("Left"):
                left = b_turt.xcor() - 5
                b_turt.goto(left, -350)
 
            # mapping Ctrl to control faster movement    
            if keyboard.is_pressed("Ctrl"):
                if keyboard.is_pressed("Right"):
                    right = b_turt.xcor() + 30
                    b_turt.goto(right, -350)
                if keyboard.is_pressed("Left"):
                    left = b_turt.xcor() - 30
                    b_turt.goto(left, -350)
                   
            if keyboard.is_pressed('Enter'):
                target.color("black")
                target.penup()
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                target.goto(x, y)
                print(target.pos)
            if b_turt.ycor() - 25 <= target.ycor() <= b_turt.ycor() + 25 and b_turt.xcor() - 25 <= target.xcor() <= b_turt.xcor() + 25:
                target.color("white")
                score = score + 1
                write()
 
                   
                   
               
 
                             
   
 
wn = trtl.Screen()
wn.mainloop()
 
 
 

