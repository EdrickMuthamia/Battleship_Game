# -----------------------------------
# Branch: kiptoo-battle
# -----------------------------------

while True:
    # Player's turn
    dragon_hp = dragon_hp - my_damage
    print(f"The {char} damaged the Dragon!")
    print(f"Dragon's HP is now: {dragon_hp}")

    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break

    # Dragon's turn
    player_hp = player_hp - dragon_damage
    print(f"The Dragon damaged the {char}!")
    print(f"{char}'s HP is now: {player_hp}\n")

    if player_hp <= 0:
        print(f"The {char} has lost the battle!")
        break
