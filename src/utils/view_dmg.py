def view_dmg (damage_dealt, damage_taken):

    print("Danos causados:\n")
    print('\n')
    for target, damage in damage_dealt.items():
        print(f"{target}\n")
        for type_damage, total in damage.items():
            print(f"{type_damage} - {total:.2f}\n")
        print("\n")

    print("Danos sofridos:\n")
    print('\n')
    for target, damage in damage_taken.items():
        print(f"{target}\n")
        for type_damage, total in damage.items():
            print(f"{type_damage} - {total:.2f}\n")
        print("\n")