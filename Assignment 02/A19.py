import random


def guess_random_number():
    random_number = random.randint(1, 100)
    print(f"The random number is: {random_number}")
    print("You have one attempt to guess the number between 1 and 100:")

    guess = int(input("Enter your guess:"))

    if guess == random_number:
        print("You guessed it! Congratulations!")
    else:
        print("Sorry, you didn't guess correctly. The random number was:", random_number)


guess_random_number()