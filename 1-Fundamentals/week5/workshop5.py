"""
Week 5 workshop
By: Shosuke Doi
Version 1.3
Last Updated: 10/28/2023
"""

import random


# Task 1: Guess the number through user input
def guess_random_number(tries, start, stop):
    # Generate a random target number within the specified range
    random_number = random.randint(start, stop)

    while tries > 0:
        print(f"Number of tries left {tries}")
        user_input = input("Guess a number between 0 an 10: ")

        guess = int(user_input)

        if guess == random_number:
            print("You guessed the correct number")
            return
        if guess < random_number:
            print("Guess higher!")
        if guess > random_number:
            print("Guess lower!")

        tries = tries - 1

    print("You have failed to guess the number")
    return


# Task 2: Guess the number programmatically through linear search
def guess_random_num_linear(tries, start, stop):
    # Generate a random target number within the specified range
    target = random.randint(start, stop)

    for guess in range(tries):
        print(f"Computer's guess: {guess}")

        if guess == target:
            print("Computer guessed the correct number!")
            return
        elif guess < target:
            print("Computer's guess is too low.")
        else:
            print("Computer's guess is too high.")

    print("Out of guesses. Computer couldn't find the target number.")
    return


# Task 3: Guess the number programmatically using binary search.
def guess_random_num_binary(tries, start, stop):
    # Generate a random target number within the specified range
    target = random.randint(start, stop)

    lower_bound = start
    upper_bound = stop

    for attempt in range(1, tries + 1):
        guess = (lower_bound + upper_bound) // 2
        print(f"Attempt {attempt}: Computer's guess is {guess}")

        if guess == target:
            print("You guessed the correct number")
            return
        if guess < target:
            lower_bound = guess + 1
            print("Guess higher!")
        else:
            upper_bound = guess + 1
            print("Guess lower!")
    print("You have failed to guess the number")
    return


# Test functions
guess_random_number(5, 0, 10)
guess_random_num_linear(5, 0, 10)
guess_random_num_binary(5, 0, 100)
