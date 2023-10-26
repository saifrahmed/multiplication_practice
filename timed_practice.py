import random
import time
import json
import os.path
import datetime


HIGH_SCORE_FILE = './high_scores.json'

# in seconds
PRACTICE_TIME_LIMIT = 5

POINTS_FOR_RIGHT_ANSWER = 3
POINTS_FOR_WRONG_ANSWER = -1

base_number = 8
total_points = 0
num_right = 0
num_wrong = 0


player_name = input("Your name: ")

start_time = time.time()

while True:
    current_time = time.time()
    if current_time - start_time > PRACTICE_TIME_LIMIT:
        print(f"Time's up!\n\n")
        break

    factor_2 = random.randint(0, 10)
    answer = base_number * factor_2
    print(f"\n\n\nWhat is {base_number} * {factor_2} = ?")
    user_answer = int(input("Your answer: "))
    if user_answer == answer:
        total_points += POINTS_FOR_RIGHT_ANSWER
        print(f"Correct! Good job! you have {total_points} points! ")
        num_right += 1
    else:
        total_points += POINTS_FOR_WRONG_ANSWER
        print(f"{base_number} * {factor_2} = {base_number * factor_2}")
        print(f"Incorrect! You have {total_points} points!")
        num_wrong += 1

    print(f"You have {PRACTICE_TIME_LIMIT - (current_time - start_time):3.0f} seconds left!")

current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

game_results = {
   "player_name": player_name,
    "total_points": total_points,
    "num_right": num_right,
    "num_wrong": num_wrong,
    "game_date": formatted_time[:-3]
    }
print(f"Game over, you end with {total_points} points!")
print(f"\tPlayer name: {player_name}")
print(f"\tCorrect answers: {num_right}")
print(f"\tIncorrect answers: {num_wrong}")
print(f"\tTotal time: {PRACTICE_TIME_LIMIT}")





high_scores = {}
check_file = os.path.isfile(HIGH_SCORE_FILE)
if check_file:
  with open(HIGH_SCORE_FILE) as high_scores_file:
    high_scores = json.load(high_scores_file)

if str(PRACTICE_TIME_LIMIT) not in high_scores or \
    int(high_scores[str(PRACTICE_TIME_LIMIT)]["total_points"]) < total_points:
  high_scores[str(PRACTICE_TIME_LIMIT)] = game_results
  print(f"New high score for {PRACTICE_TIME_LIMIT} seconds! Record held by {player_name} with {total_points} points!")
else:
    print(f"Sorry, you didn't beat the high score of {high_scores[str(PRACTICE_TIME_LIMIT)]['total_points']} points held by {high_scores[str(PRACTICE_TIME_LIMIT)]['player_name']}")
    
# Writing to sample.json
with open(HIGH_SCORE_FILE, "w") as outfile:
    outfile.write(json.dumps(high_scores, indent=4))
