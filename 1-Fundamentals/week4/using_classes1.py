class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print(player1.name)
print(player2.hp)
