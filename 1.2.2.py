import turtle as trtl
import random
import time
import leaderboard as lb

# leaderboard variables
leaderboard_file_name = "leaderboard1.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot


  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, target, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, target, score)



font_setup = ("Arial", 20, "normal")
timer = 5
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
    manage_leaderboard()
    
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
    if timer_up == False:
        global score
        score = score + 1
        target.penup()
        x = random.randint(-270, 290)
        y = random.randint(-270, 290)
        size = random.randint(1, 10)
        target.shapesize(size)
        target.goto(x, y)
        write()
    elif timer_up == True:
        quit()
    
        
    
def start_game():
    target.onclick(clicked)
    counter.getscreen().ontimer(countdown, counter_interval)
start_game()



wn = trtl.Screen()
wn.mainloop()
 
 
 

