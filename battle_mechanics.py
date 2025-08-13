from battlegame import Character, Dragon, setup_game_stats

# -----------------------------------
# Battle with the Dragon
# -----------------------------------
def battle_begins(player: Character, dragon: Dragon):
    while True:
        # Player attacks
        dragon.hp -= player.damage
        print(f"{player.name} attacked the Dragon for {player.damage} damage!")
        print(f"Dragon's HP is now: {dragon.hp}")

        if dragon.hp <= 0:
            print("The Dragon has been defeated! You win!")
            break

        # Dragon attacks
        player.hp -= dragon.damage
        print(f"The Dragon attacked {player.name} for {dragon.damage} damage!")
        print(f"{player.name}'s HP is now: {player.hp}\n")

        if player.hp <= 0:
            print(f" {player.name} has fallen. You lose!")
            break