import json

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
        exit()
    elif opt1 == '0':
        exit()

def name_check():
    global name

    with open('file.json') as user_file:
        file_contents = user_file.read() # Läser in json filen till skriptets minne. 
    print(file_contents)
    
    name = input("Enter your unique name  : ")
    while name in file_contents: # Loopar tills spelaren har skrivit in ett unikt namn.
        print("That name is all ready taken!")
        name = input("Enter your unique name  : ")
    else:
        character_create()

def character_create():
    global name # För att använda oss av variabeln i name_check funktionen. Inte det snyggaste men funkar...

    print('What is your roll?\n 1. Knight \n 2. Mage')
    roll_opt = input(": ")
    if roll_opt == '1':
        hp = 35
        roll = "knight"
        weapon = "sword"
    elif roll_opt == '2':
        hp = 15
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

title_screen_print()