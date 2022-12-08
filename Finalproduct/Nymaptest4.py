import random
import json
import os 
def title_screen_print():
    print("")
    print("#########################################")
    print("######## WELCOME TO DUNGEON RUN #########")
    print("#########################################")
    print("")
    print(" Please choose one of the following alternatives")
    print ("")
    print ("[1]<---- Create a new hero")
    print ("")
    print ("[2]<---- Choose an existing hero")
    print ("")
    print ("[0]<---- Exit the game")
    title_screen_options()

def title_screen_options():
    opt1 = input("Enter your option   : ")
    if opt1 == '1':
        name_check()
    elif opt1 == '2':
        char_load()
    elif opt1 == '0':
        exit()
def char_load():
  global name
  database = "file.json"
  data = json.loads(open(database).read())

  print("Characters:")
  print(data)
  char_opt = input("Choose character: ")

  for item in data:
      if item["name"] == char_opt:
        name = item['name']
        appearence = item['apperance'] 
        roll = item['roll']
        print('You are ' + name + ', the ' + appearence + ' ' + roll + '.')

#char_load()
def name_check():
    global name

    name = input("Enter your name  : ")
    with open('file.json') as user_file:
        file_contents = user_file.read() # Läser in json filen till skriptets minne. 
        print(file_contents)
    while name in file_contents: # Loopar tills spelaren har skrivit in ett unikt namn.
        print("That name is all ready taken!")
        name = input("Enter your name  : ")
    else:
        character_create()

def character_create():
    global name # För att använda oss av variabeln i name_check funktionen. Inte det snyggaste men funkar...

    print('What is your roll?\n 1. Knight \n 2. Mage')
    roll_opt = input(": ")
    if roll_opt == '1':
        roll = "knight"
        weapon = "sword"
    elif roll_opt == '2':
        roll = "mage"
        weapon = "staff"

    print ("Choose your apperance:\n 1. Muscular\n 2. Meager \n 3. Ragged\n 4. Bald ")
    app_opt = input (": ")
    if app_opt == '1':
        appearence = "muscular"
    elif app_opt == '2':
        appearence = "meager"
    elif app_opt == '3':
        appearence = "ragged"
    elif app_opt == '4':
        appearence = "bald"

# Sparar spelarens val (namn, utseende och roll) till en json-fil.
    fname = "file.json"
    player_stats = {
        "name": name,
        "apperance": appearence,
        "roll": roll
    }
    with open(fname) as feedsjson:
        feeds = json.load(feedsjson)

    feeds.append(player_stats)
    with open(fname, mode='w') as f:
        f.write(json.dumps(feeds))

    print('You are ' + name + ', the ' + appearence + ' ' + roll + '. You wield a ' + weapon + '.\nYou enter a dungeon.')

# Här kan vi möjligtvis lägga in ett simpelt stridssystem där användaren direkt möter ett monster när hen går in i dungeonen.

def start1():
    global name
    world_map = [
    [' ', ' ', ' ', ' ',],
    [' ', ' ', ' ', ' ',],
    [' ', ' ', ' ', ' ',],
    [' ', ' ', ' ', ' ',]
    ]
    def battle():
        global name
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
        while ehp > 0:
            print("")
            print(f"{name} HP is: {hp}")
            print(f"{mon_print} HP: {ehp}")
            print("(1)Attack\n(2)Defend")
            actions = int(input("Choose your action: "))
            actionsai = 1,2
            aiactions = random.choice(actionsai)
            if actions == 1 and aiactions == 1:
                ehp = (ehp-dmg)
                hp = (hp-edmg)
                print(f"{name} attacked and dealt {dmg} damage\nThe {mon_print} dealt {edmg} damage")

            elif actions == 2 and aiactions == 1:
                print(f"{name} blocked the attack!")

            elif actions == 1 and aiactions == 2:
                print(f"The {mon_print} blocked the attack.")

            elif actions == 2 and actionsai == 2:
                print("You both blocked.")

            if ehp < 0 or ehp == 0:
                
                hp = (hp+edmg)
                draw_map(world_map, character_positions={})
                os.system("cls")
                print("You won!")
            elif hp == 0 and ehp == 0:
                print("Draw")
                exit()
            elif hp < 0 or hp == 0:
                print("You lose")
                exit()

    def draw_map(world_map, character_positions):
        global name
        width = len(world_map[0])
        header = "---".join(["+"] * (width + 1))  # Compute header line.
        for y, row in enumerate(world_map):
            print(header)  # Print header leading each line.
            # Figure out which characters to print in each cell.
            chars = []
            for x, c in enumerate(row):
                chars.append(str(character_positions.get((x, y), c)))
            print("| {} |".format(" | ".join(chars)))
        print(header)  # Print final header (well, footer).
    hero_position = ""
    command = input("Choose where to start:")
    if command == "NW" or command == "nw":
        hero_position = (0,0)
    if command == "NE" or command == "ne":
        hero_position = (3,0)
    if command == "SW" or command == "sw":
        hero_position = (0,3)
    if command == "SE" or command == "se":
        hero_position = (3,3)

    hero_character = '@'


    while True:
        draw_map(world_map, character_positions={
            hero_position: hero_character,
            
        })
        command = input("WASDQ?").lower()
        if command == "w" and hero_position[1] > 0:
            hero_position = (hero_position[0], hero_position[1] - 1)
        if command == "a" and hero_position[0] > 0:
            hero_position = (hero_position[0] - 1, hero_position[1])
        if command == "s" and hero_position[1] < len(world_map) - 1:
            hero_position = (hero_position[0], hero_position[1] + 1)
        if command == "d" and hero_position[0] < len(world_map[0]) - 1:
            hero_position = (hero_position[0] + 1, hero_position[1])
        if command == "q":
            break
        if hero_position == (0,1):
            print (f"You entered the dark tombs, you must face an enemy!")
            battle()
        if hero_position == (0,3):
            print ("You entered the gauntlet of fire, prepare to battle!")
            battle()
        if hero_position == (1,0):
            print ("You entered the shadow prison, you must fight!")
            battle()
        if hero_position == (1,2):
            print ("You entered the hellthrone, demons are upon you!")
            battle()
        if hero_position == (1,3):
            print ("You entered the demonic portal, Face your worst nightmare!")
            battle()
        if hero_position == (2,1):
            print ("You entered the shadow caves, earn your right to pass!")
            battle()
        if hero_position == (2,2):
            print ("You entered the throne of kings, show your worth!")
            battle()
        if hero_position == (3,0):
            print ("You entered the gates of the underworld, fight for your life!")
            battle()
        if hero_position == (3,3):
            print ("You entered the castle, only one will prevail!")
            battle()
def start2():
    world_map = [
    [' ', ' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ',]
    ]
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
        while ehp > 0:
            print("")
            print(f"{name} HP: {hp}")
            print(f"{mon_print} HP: {ehp}")
            print("(1)Attack\n(2)Defend")
            actions = int(input("Choose your action: "))
            actionsai = 1,2
            aiactions = random.choice(actionsai)
            if actions == 1 and aiactions == 1:
                ehp = (ehp-dmg)
                hp = (hp-edmg)
                print(f"{name} attacked and dealt {dmg} damage\nThe {mon_print} dealt {edmg} damage")

            elif actions == 2 and aiactions == 1:
                print(f"{name} blocked the attack!")

            elif actions == 1 and aiactions == 2:
                print(f"The {mon_print} blocked the attack.")

            elif actions == 2 and actionsai == 2:
                print("You both blocked.")

            if ehp < 0 or ehp == 0:
                
                hp = (hp+edmg)
                draw_map(world_map, character_positions={})
                os.system("cls")
                print("You won!")
            elif hp == 0 and ehp == 0:
                print("Draw")
                exit()
            elif hp < 0 or hp == 0:
                print("You lose")
                exit()

    def draw_map(world_map, character_positions):
        width = len(world_map[0])
        header = "---".join(["+"] * (width + 1))  # Compute header line.
        for y, row in enumerate(world_map):
            print(header)  # Print header leading each line.
            # Figure out which characters to print in each cell.
            chars = []
            for x, c in enumerate(row):
                chars.append(str(character_positions.get((x, y), c)))
            print("| {} |".format(" | ".join(chars)))
        print(header)  # Print final header (well, footer).
    hero_position = ""
    command = input("Choose where to start:")
    if command == "NW" or command == "nw":
        hero_position = (0,0)
    if command == "NE" or command == "ne":
        hero_position = (4,0)
    if command == "SW" or command == "sw":
        hero_position = (0,4)
    if command == "SE" or command == "se":
        hero_position = (4,4)

    hero_character = '@'


    while True:
        draw_map(world_map, character_positions={
            hero_position: hero_character,
            
        })
        command = input("WASDQ?").lower()
        if command == "w" and hero_position[1] > 0:
            hero_position = (hero_position[0], hero_position[1] - 1)
        if command == "a" and hero_position[0] > 0:
            hero_position = (hero_position[0] - 1, hero_position[1])
        if command == "s" and hero_position[1] < len(world_map) - 1:
            hero_position = (hero_position[0], hero_position[1] + 1)
        if command == "d" and hero_position[0] < len(world_map[0]) - 1:
            hero_position = (hero_position[0] + 1, hero_position[1])
        if command == "q":
            break
        if hero_position == (0,1):
            print ("You entered the dark tombs, you must face an enemy!")
            battle()
        if hero_position == (0,3):
            print ("You entered the gauntlet of fire, prepare to battle!")
            battle()
        if hero_position == (1,0):
            print ("You entered the shadow prison, you must fight!")
            battle()
        if hero_position == (1,2):
            print ("You entered the hellthrone, demons are upon you!")
            battle()
        if hero_position == (1,3):
            print ("You entered the demonic portal, Face your worst nightmare!")
            battle()
        if hero_position == (1,4):
            print ("You entered the shadowlands, can you face death?!")
            battle()
        if hero_position == (2,1):
            print ("You entered the shadow caves, earn your right to pass!")
            battle()
        if hero_position == (2,2):
            print ("You entered the throne of kings, show your worth!")
            battle()
        if hero_position == (2,4):
            print ("You entered the butchers room, slaughter awaits you!")
            battle()
        if hero_position == (3,0):
            print ("You entered the gates of the underworld, fight for your life!")
            battle()
        if hero_position == (3,3):
            print ("You entered the castle, only one will prevail!")
            battle()
        if hero_position == (3,4):
            print ("You entered the ruins of doom, wrath is upon you!")
            battle()
        if hero_position == (4,0):
            print ("You entered the castle gates, you will perish!")
            battle()
        if hero_position == (4,2):
            print ("You entered the prison of hell, face eternal damnation!")
            battle()
        if hero_position == (4,4):
            print ("You entered the blood dungeon, your enemy awaits you!")
            battle()
        

def start3():
    world_map = [
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',],
    [' ', ' ', ' ', ' ',' ', ' ', ' ',' ',]
    ]
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
        while ehp > 0:
            print("")
            print(f"{name} HP: {hp}")
            print(f"{mon_print} HP: {ehp}")
            print("(1)Attack\n(2)Defend")
            actions = int(input("Choose your action: "))
            actionsai = 1,2
            aiactions = random.choice(actionsai)
            if actions == 1 and aiactions == 1:
                ehp = (ehp-dmg)
                hp = (hp-edmg)
                print(f"{name} attacked and dealt {dmg} damage\nThe {mon_print} dealt {edmg} damage")

            elif actions == 2 and aiactions == 1:
                print(f"{name} blocked the attack!")

            elif actions == 1 and aiactions == 2:
                print(f"The {mon_print} blocked the attack.")

            elif actions == 2 and actionsai == 2:
                print("You both blocked.")

            if ehp < 0 or ehp == 0:
                
                hp = (hp+edmg)
                draw_map(world_map, character_positions={})
                os.system("cls")
                print("You won!")
            elif hp == 0 and ehp == 0:
                print("Draw")
                exit()
            elif hp < 0 or hp == 0:
                print("You lose")
                exit()

    def draw_map(world_map, character_positions):
        width = len(world_map[0])
        header = "---".join(["+"] * (width + 1))  # Compute header line.
        for y, row in enumerate(world_map):
            print(header)  # Print header leading each line.
            # Figure out which characters to print in each cell.
            chars = []
            for x, c in enumerate(row):
                chars.append(str(character_positions.get((x, y), c)))
            print("| {} |".format(" | ".join(chars)))
        print(header)  # Print final header (well, footer).
    hero_position = ""
    command = input("Choose where to start:")
    if command == "NW" or command == "nw":
        hero_position = (0,0)
    if command == "NE" or command == "ne":
        hero_position = (7,0)
    if command == "SW" or command == "sw":
        hero_position = (0,7)
    if command == "SE" or command == "se":
        hero_position = (7,7)

    hero_character = '@'


    while True:
        draw_map(world_map, character_positions={
            hero_position: hero_character,
            
        })
        command = input("WASDQ?").lower()
        if command == "w" and hero_position[1] > 0:
            hero_position = (hero_position[0], hero_position[1] - 1)
        if command == "a" and hero_position[0] > 0:
            hero_position = (hero_position[0] - 1, hero_position[1])
        if command == "s" and hero_position[1] < len(world_map) - 1:
            hero_position = (hero_position[0], hero_position[1] + 1)
        if command == "d" and hero_position[0] < len(world_map[0]) - 1:
            hero_position = (hero_position[0] + 1, hero_position[1])
        if command == "q":
            break
        if hero_position == (0,1):
            print ("You entered the dark tombs, you must face an enemy!")
            battle()
        if hero_position == (0,3):
            print ("You entered the gauntlet of fire, prepare to battle!")
            battle()
        if hero_position == (0,6):
            print ("You entered the blood gates, you are alone!")
            battle()
        if hero_position == (1,0):
            print ("You entered the shadow prison, you must fight!")
            battle()
        if hero_position == (1,2):
            print ("You entered the hellthrone, demons are upon you!")
            battle()
        if hero_position == (1,3):
            print ("You entered the demonic portal, Face your worst nightmare!")
            battle()
        if hero_position == (1,6):
            print ("You entered the shadowlands, can you face death?!")
            battle()
        if hero_position == (2,1):
            print ("You entered the shadow caves, earn your right to pass!")
            battle()
        if hero_position == (2,2):
            print ("You entered the throne of kings, show your worth!")
            battle()
        if hero_position == (2,5):
            print ("You entered the butchers room, slaughter awaits you!")
            battle()
        if hero_position == (2,7):
            print ("You entered the lions mouth, show yourself!")
            battle()
        if hero_position == (3,0):
            print ("You entered the gates of the underworld, fight for your life!")
            battle()
        if hero_position == (3,3):
            print ("You entered the castle, only one will prevail!")
            battle()
        if hero_position == (3,6):
            print ("You entered the ruins of doom, wrath is upon you!")
            battle()
        if hero_position == (4,0):
            print ("You entered the castle gates, you will perish!")
            battle()
        if hero_position == (4,2):
            print ("You entered the prison of hell, face eternal damnation!")
            battle()
        if hero_position == (4,4):
            print ("You entered the blood dungeon, your enemy awaits you!")
            battle()
        if hero_position == (4,7):
            print ("You entered the slaughterhouse, demonic forces attacks!")
            battle()
        if hero_position == (5,1):
            print ("You entered the dark zones, evil rests here!")
            battle()
        if hero_position == (5,3):
            print ("You entered the realm of plague, you will not survive!")
            battle()
        if hero_position == (5,7):
            print ("You entered the graves of the kings, only the strongest survives!")
            battle()
        if hero_position == (6,2):
            print ("You entered the realm of death, you must overcome fear!")
            battle()
        if hero_position == (6,4):
            print ("You entered the dungeons of orcs, only the most savage survives!")
            battle()
        if hero_position == (6,6):
            print ("You entered the evil planes, battle for survival!")
            battle()
        if hero_position == (7,0):
            print ("You entered the throne of terror, here lies darkness!")
            battle()
        if hero_position == (7,3):
            print ("You entered the summoning stones, arcanish enemies attacks!")
            battle()
        if hero_position == (7,5):
            print ("You entered the arcane gates, a never before seen enemy!")
            battle()
        if hero_position == (7,7):
            print ("You entered the graves of the undeath, your courage will not suffice!")
            battle()
         


title_screen_print()
#while True:
lala = input("Choose your mapsize: ")
if lala == "Small" or lala == "small":
            start1()
if lala == "Medium" or lala == "medium":
            start2()
if lala == "Large" or lala == "large":
            start3()