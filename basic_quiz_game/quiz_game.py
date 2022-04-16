import random
import traceback

print("Welcome to the quiz.!")

questions = [{"Question": "What does CPU stands for.? ", "Answer": "central processing unit"},
             {"Question": "What does GPU stands for? ", "Answer": "graphics processing unit"},
             {"Question": "What does RAM stands for? ", "Answer": "random access memory"},
             {"Question": "What does PSU stands for? ", "Answer": "power supply"}]


def validate_user_response():
    try:
        if playing.lower() != "yes":
            print("Thank you, Good Bye.!")
            quit()
        else:
            print("Okay! Let's play :)")
            result = quiz()
        return str(result)
    except Exception:
        print(traceback.format_exc())


def quiz():
    score = 0
    for i in questions:
        answer = input(i['Question'] + "\n").lower()
        if answer == i['Answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    return str(score)


playing = input("Do you want to play.? (yes/no)\n")

print(f"Thank you for playing the game. \nYou have got {str(validate_user_response())} questions correct.!")
