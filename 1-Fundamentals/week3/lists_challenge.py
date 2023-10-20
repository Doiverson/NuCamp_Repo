import random

diamonds = [
    "AD",
    "2D",
    "3D",
    "4D",
    "5D",
    "6D",
    "7D",
    "8D",
    "9D",
    "10D",
    "JD",
    "QD",
    "KD",
]
statements = {
    0: "Press Enter to pick a card, or 'Q' then enter to quit: ",
    1: "Hand: ",
    3: "Remaining",
    4: "No cards left.",
    5: [],
}
for cycle in range(13):
    if input(statements[0]) in ["Q", "q"]:
        quit()
    statements[5].append(random.choice(diamonds))
    # this is list-comprehension
    diamonds = [card for card in diamonds if card not in statements[5]]
    print(statements[1], statements[5], "\n", statements[3], diamonds)
    if len(diamonds) == 0:
        print(statements[4])
