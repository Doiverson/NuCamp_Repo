wizard = "Wizard"
elf = "ELF"
human = "HUMAN"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
drgon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    userInput = input("Choose your character: ")

    if userInput == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif userInput == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif userInput == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break

    print("Unknown character")

print("Character: " + character)
print("My HP:", my_hp)
print("My Damage:", my_damage, "\n")

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now", dragon_hp, "\n")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    print("The Dragon strikes back at", character)
    my_hp = my_hp - drgon_damage
    print("The " + character + "'s hitpoints are now", my_hp, "\n")

    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
