import random


def dice_game():
    high_score = 0
    while True:
        print(f"Current High Score: {high_score}")
        print("1) Roll Dice")
        print("2) Leave Game")
        userInput = input("Enter Your Choice")
        if userInput == "1":
            randomNumber1 = random.randint(1, 6)
            randomNumber2 = random.randint(1, 6)
            total = randomNumber1 + randomNumber2

            print(f"You rall a {randomNumber1}")
            print(f"You rall a {randomNumber2}")
            print(f"You have rolled a total of {total}")

            if high_score < total:
                high_score = total
                print("New High Score!")

        if userInput == "2":
            break


dice_game()
