import random


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
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay.! The computer guessed your number, {guess}, correctly!")


computer_guess(100)
