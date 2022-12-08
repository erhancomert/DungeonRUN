import random # Gör så att vi kan implementera slumpen i striderna.  

def item_pouch():
    item_pouch.gold = 0

def battle():
    hp = 20
    dmg = random.randint(5,20)  # Skriptet väljer en slumpvald siffra, till exempel från 5 till 20. 

    monsters = ["Skeleton", "Troll"]
    mon_print = random.choice(monsters)
    if mon_print == "Skeleton":
        ehp = 12
        edmg = random.randint(3,10)
    elif mon_print == "Troll":
        ehp = 15
        edmg = random.randint(4,14)

    print(f"You've encountred a {mon_print}!")
    while ehp > 0:    
        print("")
        print(f"Your HP: {hp}")
        print(f"{mon_print} HP: {ehp}")
        print("")
        print("(1)Attack\n(2)Defend")
        print("")
        actions = int(input("Choose your action: "))
        actionsai = 1,2
        aiactions = random.choice(actionsai)
        if actions == 1 and aiactions == 1:
            ehp = (ehp-dmg)
            hp = (hp-edmg)
            print(f"You attacked and dealt {dmg} damage\nThe enemy dealt {edmg} damage")

        elif actions == 2 and aiactions == 1:
            print("You blocked the attack!")

        elif actions == 1 and aiactions == 2:
            print("The enemy blocked the attack.")

        elif actions == 2 and actionsai == 2:
            print("You enemy blocked.")

        if ehp < 0 or ehp == 0:
            print("")
            print("You won!")
            hp = (hp+edmg)
            item_pouch.gold += random.randint(1,20)
            print(f"You got {item_pouch.gold} gold coins!")
            if item_pouch.gold == 10 or item_pouch.gold > 10:
                print(f"Total hp:{hp}")
                print("Restore 15 hp for 10 gold coins?\n(1) Yes.\n(2) No.")
                action = int(input("Choose(1-2): "))
                if action == 1:
                    item_pouch.gold -= 10
                    hp += 15
                    print(f"You restored 15 hp and have {item_pouch.gold} gold coins left!")
                elif action == 2:
                    pass
        elif hp == 0 and ehp == 0:
            print("Draw")
            exit()
        elif hp < 0 or hp == 0:
            print("You lose")
            exit()
item_pouch()
battle()