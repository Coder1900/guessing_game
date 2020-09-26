import random
import my_input_library as myinputs

# creates a random number and asks user to guess it
# the input is the number range to guess_random_number
# output is number of trys
def guess_random_number(upper_limit):
  trys = 0
  guess = ""
  number_generator = random.randint(0, upper_limit)

  while guess != number_generator:
    #print(number_generator) # debugging message
    msg = "Guess the number between 0 - " + str(upper_limit) + ": "
    guess = myinputs.get_input(msg)
    trys += 1
  
    if guess < number_generator: 
      print("Incorrect you had to guess a bigger number")
      
    elif guess > number_generator:
      print("Incorrect you had to guess a smaller number")
      
    elif guess == number_generator:
      print("correct")
      score = (f"It took you {trys} attempts to guess the correct number" )
      print(score)
      return trys
    # if user takes more then 9 trys to guess the round ends    
    if trys >= 9:
      return trys

# main function that runs the game
def run_game():

  my_high_score = 9     # init the high score to the lowest score

  # asks user for game level and checks if it is greater then 0
  while 1:
   guess_range = myinputs.game_level()
   if guess_range > 0:
     break
  
  # while the user wants to continue play the game
  while 1:
    all_time_high_score_of_level = get_high_score(guess_range)
    attemps = (guess_random_number(guess_range))

    if attemps < my_high_score:
      my_high_score = attemps

    print(f"Your score is {attemps} and your high score was {my_high_score} ")
    
    if my_high_score < all_time_high_score_of_level:
      print(f"You beat the all time high score which was {all_time_high_score_of_level}")
      records_high_scores(guess_range, my_high_score)
    else:
      print(f"Try to beat all time high score which is {all_time_high_score_of_level}")

    print("")
    print("Do you want to continue or change level or quit? ")
    user_continue = input("Please enter continue or change or quit: ")
    print("")

    if user_continue.lower() == "change":
      while 1:
        guess_range = myinputs.game_level()
        if guess_range > 0:
          break
    elif user_continue.lower() != "continue":
      break

# function that gets high score and returns it
def get_high_score(level):
  high_scores_array = myinputs.reads_high_scores()
  while 1:
    if level == 10:
      return high_scores_array[0]
    elif level == 25:
      return high_scores_array[1]
    elif level == 50:
      return high_scores_array[2]

# stores the high score in a variable
def records_high_scores(level, high_score):
  high_scores_array = myinputs.reads_high_scores()
  
  if level == 10:
    high_scores_array[0] = high_score
  elif level == 25:
    high_scores_array[1] = high_score
  elif level == 50:
    high_scores_array[2] = high_score
 
  myinputs.stores_high_scores(high_scores_array)  


## Main function
print("############################")
print("Welcome to number guessing game")
print("Designed by: Solomon")
print("############################")
print("")
run_game()
    