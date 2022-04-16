import random


def guess_num(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low..")
        if guess > random_number:
            print("Sorry, guess again. Too high..")
    print(f"Yay, Congratulation. You have guessed the number {random_number} correctly")


guess_num(100)

# computer has to guess the number for us.
def computer_guess(y):
    low = 1
    high = y
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C) ??").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay.! The computer guessed your number, {guess}, correctly!")


# guess_num(10)
computer_guess(100)
