if character_choice == "1":
        char = wizard
        player_hp = wizard_hp
        my_damage = wizard_damage
        break
     elif character_choice == "2":
        char = elf
        player_hp = elf_hp
        my_damage = elf_damage
        break
     elif character_choice == "3":
        char = human
        player_hp = human_hp
        my_damage = human_damage
        break
else:
        print("Invalid choice. Please try again.\n")

print(f"\nYou have chosen the {char}!\n")