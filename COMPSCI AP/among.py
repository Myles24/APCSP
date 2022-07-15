
file_name = "leaderboard.txt"
# load leaderboard from file
def load_leaderboard(file_name, leader_names, leader_scores):

  leaderboard_file = open("leaderboard.txt", "r")  # need to create the file ahead of time in same folder

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  for line in leaderboard_file:
    leader_name = ""
    leader_score = ""    
    index = 0

    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
    print(line)