import sys
import random

question_list=[
    ("Florida", "What state is Disney World in?"),
    ("Iowa", "What state is the Field of Dreams in?"),
    ("Garden State", "What is New Jersey's nickname?"),
    ("Big Apple", "What is New York's nickname?"),
    ("Cat", "What is the second most popular pet in the US?"),
]



print("\n\n\n\n")
name = input ("What is your name? ")
print(f"Hello {name}, welcome to the facts game! Answer a question correctly and you get 3 points. Answer incorrectly and you lose 1 point. You have 30 seconds to answer as many questions as you can. Good luck!")

def game():
    points = 0
    random.shuffle(question_list)
    for (random_a, random_q) in question_list:
        print("\n")
        print(random_q)
        userinput = input("Your answer: ")
        if userinput.upper() == random_a.upper():
            print("Correct! You have 3 points!")
            points += 3
        else: 
            print(f"Incorrect! You lose 1 point! The correct answer is {random_a}")
            points -= 1

    print(f"Game over! You have {points} points!")
    sys.exit()

    
while True:
    userinput = input ("Type START to start the game. ")
    if userinput.upper() == "START":
        game()

    else:
        print("Wait what?! Type START!")

    if userinput.upper() == "END":
        print("See you next time!")
        sys.exit()

