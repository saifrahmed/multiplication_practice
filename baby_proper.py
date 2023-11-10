import sys
import random

question_list=[
    ("Florida", "What state is Disney World in?"),
    ("Iowa", "What state is the Field of Dreams in?"),
    ("Garden State", "What is New Jersey's nickname?"),
    ("Big Apple", "What is New York's nickname?"),
    ("Cat", "What is the second most popular pet in the US?"),
    ("Origami", "What is the Japanese art of paper folding called?"),
    ("X", "What is Twitter's new name?"),
    ("Pikachu", "A yellow Pokemon with red cheeks and a lightning bolt tail."),
    ("Stone", "Harry Potter and the Sorcerer's ________"),
    ("Chocolate", "What is the most common use to use cocoa beans?"),
    ("WhatsApp", "A messaging app owned by Facebook."),
    ("Donkey", "What is animal is Shrek's best friend?"),
    ("Kangaroo", "What animal has a pouch?"),
    ("Pig", "What animal is Peppa?"),
    ("Dinosaur", "What animal is Barney?"),
    ("Cheetah", "What animal is the fastest land animal?"),
    ("Dolphin", "What animal is the smartest in the ocean?"),
    ("Giraffe", "What animal has the longest neck?"),
    ("Elephant", "What animal has the longest nose?"),
    ("Hippo", "What animal has the largest mouth?"),
    ("Penguin", "What animal is Happy Feet?"),
    ("Panda", "What animal is Po?"),
    ("Lion", "What animal is Simba?"),
    ("Bear", "What animal is Winnie the Pooh?"),
    ("Monkey", "What animal is Curious George?"),
    ("Rabbit", "What animal is Bugs Bunny?"),
    ("Mouse", "What animal is Mickey Mouse?"),
    ("Frog", "What animal is Kermit?"),
    ("Spongebob", "Who lives in a pineapple under the sea?"),
    ("Patrick", "Who is Spongebob's best friend?"),
    ("Squidward", "Who is Spongebob's neighbor?"),
    ("Sandy", "Who is Spongebob's friend that is a squirrel?"),
    ("Mr. Krabs", "Who is Spongebob's boss?"),
    ("Plankton", "Who is Spongebob's enemy?"),
    ("Gary", "Who is Spongebob's pet?"),

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

