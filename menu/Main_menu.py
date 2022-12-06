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
        character_create()
    elif opt1 == '2':
        exit()
    elif opt1 == '0':
        exit()

def character_create():
    name = input("Enter your name  : ")
    
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

    print('You are ' + name + ', the ' + appearence + ' ' + roll + '. You wield a ' + weapon + '.\nYou enter a dungeon.')

# Här kan vi möjligtvis lägga in ett simpelt stridssystem där användaren direkt möter ett monster när hen går in i dungeonen.

title_screen_print()