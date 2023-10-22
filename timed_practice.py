import random
import time

# in seconds
PRACTICE_TIME_LIMIT = 30

POINTS_FOR_RIGHT_ANSWER = 3
POINTS_FOR_WRONG_ANSWER = -1

base_number = 8
total_points = 0
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
    else:
        total_points += POINTS_FOR_WRONG_ANSWER
        print(f"{base_number} * {factor_2} = {base_number * factor_2}")
        print(f"Incorrect! You have {total_points} points!")
    print(f"You have {PRACTICE_TIME_LIMIT - (current_time - start_time):3.0f} seconds left!")

print(f"Game over, you end with {total_points} points!")