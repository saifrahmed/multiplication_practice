import random

NUM_PRACTICE_PROBLEMS  = 15

POINTS_FOR_RIGHT_ANSWER = 3
POINTS_FOR_WRONG_ANSWER = -1

base_number = 8
total_points = 0

for _ in range(NUM_PRACTICE_PROBLEMS):
    factor_2 = random.randint(0, 10)
    answer = base_number * factor_2
    print(f"\n\n\n{base_number} * {factor_2} = ?")
    user_answer = int(input("Your answer: "))
    print(f"{base_number} * {factor_2} = {base_number * factor_2}")
    if user_answer == answer:
        total_points += POINTS_FOR_RIGHT_ANSWER
        print(f"Correct! Good job! you have {total_points} points! ")
    else:
        total_points += POINTS_FOR_WRONG_ANSWER
        print(f"Incorrect! You have {total_points} points!")