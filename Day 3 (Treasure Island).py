print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

dead_end = input("You have came to a dead end! You have two options: Left or Right! Choose Wisely 0_0 : ")
dead_endinput = dead_end.lower()
if dead_endinput == "left":
    pool = input("A cliff! Swim or Wait? ")
    pool_input = pool.lower()
    if pool_input == "wait":
        print("A bus has arrived to pick you up and drop you off!")
        print("As you get off the bus you have two options...")
        door = input("Which door would you like for you destiny? Red, Blue or Yellow: ")
        door_input = door.lower()
        if door_input == "red":
            print("Burned by fire.\n Game Over :(")
        elif door_input == "blue":
            print("Eaten by beasts. \n Game Over :(")
        elif door_input == "yellow":
            print("You Win! The Treasure has been found!")
            print("")
        else:
            print("Game Over.")
    else:
        print("Game Over. :p")

else:
    print("You have fell into a hole... Game Over :(")