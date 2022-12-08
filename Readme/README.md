# Dungeon Run

Dungeon Run is a text-based adventure game where the user is either assigned a character or creates their own with the purpose of escaping the dungeon.<br>
While navigating thru the dungeon, the player needs to cross several cells.<br> 
Behind every door is a monster/troll/skeleton that needs to be defeated before entering the next cell.<br>
There are two built-in roles that the user can use to create its character, Knight and Mage.<br>
The user can also choose its characters appearence,such as Muscular,<br>
Meager, ragged or bald.<br>
During the adventure in the dungeon, there are two types of monsters that can appear, Skeleton and Troll.<br>
Damage taken and health is represented for the user during combat.
The combat system is built on a feature that randomly decides who the winner is.



# Game play instructions
## Step 1

When starting the game the user will be directed to the main menu, where the player will be given three options.
(See picture below)

![Main menu](screenshots/title_screen_1.png)


If the user wants to create a new hero, the user will be promted to write down a name for the new hero.
The new hero will be saved to a jsonfile so that the player at a later time can choose the same character.



## Step 2

To choose one of the following characters simply write down the heros name (See picture below)
.<br>
.<br>

![Character options](screenshots/title_screen_2.png)



## Step 3
The game has 3 different mapsizes (small 4x4), (medium 5x5) and (Large 8x8). 
To choose the requested size simply write down the size in letters. (See picture below)

![Map option](screenshots/title_screen_3.png)


## Step 4

In this step, the game will ask the player from wich corner of the chosen map the player wants to start from.

* Nortwest  - "nw"
* Northeast - "ne"
* Southwest - "sw"
* Southeast - "se"

To choose the requested position simply write down the two letters that represents the requested position.
(See picture below)

![corner option](screenshots/title_screen_4.png)
<br>
<br>
<br>


## Step 5 
The user now gets a graphic image of the map with the requested position to start from.
The "@" represents the heros position so that the user can see alternative routes.
To navigate in the map the user has been given four alternatives

W = Forward.<br> 
A = Left.<br>
S = Back.<br>
D = Right.<br>
Q = Quit
<br>


![Navigation map](screenshots/title_screen_5.png)
<br>
<br>
<br>

## Step 6  
When entering a cell the user faces its challenger and two alternatives are given.
<br>
<br>
1. Attack.<br>
<br>
2. Defend
<br>
<br>
The winner of the combat is not something the user can influence, as the winner is randomly chosen by the game.