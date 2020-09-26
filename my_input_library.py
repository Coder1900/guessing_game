
# checks if the user entered a number or not returns number as a interger
# program will crash if not a interger becuase of the int conversion
def get_input(msg_to_display):
  while True:
    number_str = input(msg_to_display)

    if number_str.isdecimal():
      return int(number_str)
    else:
      print("You Entered an Incorrect Number - Please Try Again")

# function to change game difficulty depending on user input
def game_level():
  print("easy = 0 - 10 medium = 0 - 25 hard = 0 - 50")
  difficulty = input("please enter easy, medium or hard: ")
  if difficulty == "easy":
    upper_limit = 10
    #print(upper_limit) # debugging message
  elif difficulty == "medium":
    upper_limit = 25
    #print(upper_limit)  # debugging message
  elif difficulty == "hard":
    upper_limit = 50
    #print(upper_limit)  # debugging message
  else:
    upper_limit = 0
  return upper_limit
  
#reads high score and returns the high scores of each level
# high score had to be less then nine as it expects only one digit for each entry
def reads_high_scores():
  high_score_file = open("high_score.txt", "r")
  high_score = high_score_file.read()
  high_score_file.close()
  high_score_array = [int(high_score[0]), int(high_score[3]), int(high_score[6])]
  return high_score_array

#stores high score for each level
def stores_high_scores(high_score):
  high_score_file = open("high_score.txt", "w")
  high_score_file.write(f"{high_score[0]}, {high_score[1]}, {high_score[2]}")
  high_score_file.close()

