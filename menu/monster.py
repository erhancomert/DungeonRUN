class Character:
    def init(self, class_name, strength, dexterity, intelligence):
        self.class_name = class_name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.health = strength*10

    def print_stats(self):
        return self.class_name + " Strength: " + str(self.strength) + " Dexterity: " + str(self.dexterity) + " Intelligence: " + str(self.intelligence)

    def print_stat_strength(self):
        return "Strength: " + str(self.strength)

    def print_stat_dexterity(self):
        return "Dexterity: " + str(self.strength)

    def print_stat_intelligence(self):
        return "Intelligence: " + str(self.strength)

    def print_stat_health(self):
        return "Max Health: " + str(self.health)

    def change_stat_strength(self, new_value):
        self.strength = new_value

    def change_stat_dexterity(self, new_value):
        self.dexterity = new_value

    def change_stat_intelligence(self, new_value):
        self.intelligence = new_value

def character_select():
    global player_class
    orc = Character("orc", 20, 10, 10)
    skellet = Character("skellet", 10, 20, 10)
    troll = Character("troll", 10, 10, 20)

    print("Welcome to TEST TEXT ADVENTURE RPG. Choose a character!")
    print("(A): " + orc.print_stats())
    print("(B): " + skellet.print_stats())
    print("(C): " + troll.print_stats())

    while True:
        user_answer = input().upper()
        if user_answer == "A":
            player_class = orc
            break
        elif user_answer == "B":
            player_class = skellet
            break
        elif user_answer == "C":
            player_class = troll
            break
        else:
            print("Invalid input! Try again.")
    print("####CHARACTER CREATION COMPLETE####")


def main():
    character_select()
    print(player_class.print_stats())

main()