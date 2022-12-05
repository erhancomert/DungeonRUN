from Options import option1
def meny():
    print("")
    print("#########################################")
    print("######## WELCOME TO DUNGEON RUN #########")
    print("#########################################")
    print("")
    print(" Please choose one of the following alternatives")
    print ("")
    print ("[0]<---- Exit the game")
    print ("")
    print ("[1]<--- Create a new hero")
    print("")
    print ("[2]<---- Choose an existing hero")
    opt = int(input("Enter your option   :"))
    return opt


usr = meny()
while usr != 0:
    if usr == 1:
        option1()
        