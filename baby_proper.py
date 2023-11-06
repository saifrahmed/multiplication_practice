import sys
import random

question_list=[
    ("Florida", "What state is Disney World in?"),
    ("Iowa", "What state is the Field of Dreams in?"),
    ("Garden State", "What is New Jersey's nickname?"),
    ("Big Apple", "What is New York's nickname?"),
    ("Cat", "What is the second most popular pet in the US?"),
]




name = input ("What is your name? ")
print(f"Hello {name}, welcome to the facts game! Answer a question correctly and you get 3 points. Answer incorrectly and you lose 1 point. You have 30 seconds to answer as many questions as you can. Good luck! Write with caps and the beginning of the word and the rest in lowercase.")

def game():
    random.shuffle(question_list)
    for (random_a, random_q) in question_list:
        print(random_q)
        userinput = input("Your answer: ")
        if userinput == random_a:
            print("Correct! You have 3 points!")
        else: 
            print(f"Incorrect! You lose 1 point! The correct answer is {random_a}")


    sys.exit()

    
while True:
    userinput = input ("Type START to start the game. ")
    if userinput == "START":
        game()

    else:
        print("Wait what?! Type START!")

    if userinput == "END":
        print("buh bye")
        sys.exit()

