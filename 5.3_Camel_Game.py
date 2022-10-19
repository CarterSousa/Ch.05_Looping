'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

print("\033[1;32m  Welcome to Quarantined Escape The current date is August 2nd, 2026. "
      " Two days ago the World ended after a modified and highly contagious strand "
      " of the Ophiocordyceps Unilateralis fungus or Zombie Ant fungus was released "
      " from a lab in Washington near the west coast, turning anyone that comes into"
      " contact with it into a violent enraged zombie.  ")
print("\033[1;32m ")
print("     Right before the electrical grid was shut down the government was able to "
      " send out a map of washington and where they would be enacting a quarantine-zone. "
      " your job is to travel 200 miles in order to escape from the quarantine zone before "
      " they shut the state off from the rest of the world. ")
print("\033[1;32m  ")
print(" \033[1;32m     You will start off with 5 drinks in your canteen and there is a 1 in 20 chance of "
      " You finding a Convenience Store. You can type E for your Status."
      " good luck and may god be with you.")
print("\033[1;32m  ")
done = False
Miles_Traveled = 0
Thirst = 0
Engine_Heat_Level = 0
Zombie_Distance = -20
Canteen_Drinks = 5
Store = random.randrange(0, 21)
Catch_Disease = random.randrange(0, 11)
date = 2
Days = 0
# LOOP
while not done:
    print("  ")
    print("(A) Drink from your canteen. ")
    print("(B) Move forward at a moderate speed. ")
    print("(C) Move forward at full speed. ")
    print("(D) Stop for the night. ")
    print("(E) Check Status. ")
    print("(Q) Quit. ")
    print("  ")

    answer = input( "\033[1;37m What steps would you like to take in order to survive.")
    # Option Q for quit
    if answer.upper() == ("Q"):
        done = True
        print("  ")
        print("\033[1;37m You Traveled :", Miles_Traveled, " Miles")
        print("  ")
        print(" \033[1;31m GAME OVER! ")
        print("  ")
    # option E for status
    elif answer.upper() == ("E"):
        print("\033[1;37m  ")
        print( "\033[1;37m Miles Traveled:",Miles_Traveled)
        print( "\033[1;37m Drinks in Canteen:",Canteen_Drinks)
        print( "\033[1;37m The zombies are currently",Zombie_Distance*-1, "Miles Behind you.")
        print("\033[1;37m  ")
    # option D for stop for the night
    elif answer.upper() == ("D"):
        Engine_Heat_Level = 0
        date += 1
        Days += 1
        Zombie_Distance += random.randrange(7, 18)
        print("\033[1;37m  ")
        print("\033[1;32m  The engine in your motorcycle has cooled down!")
        print("\033[1;37m  ")
    # option C for move ahead at full speed
    elif answer.upper() == ("C"):
        if Store == 1:
            print("\033[1;37m  ")
            print(" \033[1;32m Wow you've discovered a Convenience Store!")
            print("\033[1;37m  ")
            Engine_Heat_Level = 0
            Thirst = 0
            Canteen_Drinks = 5
        else:
            Miles_Traveled += random.randint(10, 20)
            Thirst += 2
            Engine_Heat_Level += random.randrange(1, 4)
            Zombie_Distance += random.randrange(7, 18)
    # Option B for move ahead at a moderate speed
    elif answer.upper() == ("B"):
        if Store == 1:
            print("\033[1;37m  ")
            print(" \033[1;32m Wow you've discovered a Convenience Store!")
            print("\033[1;37m  ")
            Engine_Heat_Level = 0
            Thirst = 0
            Canteen_Drinks = 5
        else:
            Miles_Traveled += random.randint(5, 12)
            Thirst += 1
            Engine_Heat_Level += 1
            Zombie_Distance += random.randrange(7, 18)
    # Option A for Drink from canteen
    elif answer.upper() == ("A"):
        Canteen_Drinks -= 1
        Thirst -= 2
        if Canteen_Drinks == 0:
            print(" \033[1;37m  ")
            print(" \033[1;33m Your canteen has no more water in it.")
            print(" \033[1;37m  ")
    # thirsty
    if not done and Thirst >= 4:
        print(" \033[1;37m  ")
        print(" \033[1;33m You are thirsty.")
        print(" \033[1;37m  ")
    # Death by thirst
    if not done and Thirst >= 6:
        print(" \033[1;37m  ")
        print(" \033[1;31m You have died of thirst")
        print(" \033[1;37m ")
        print("\033[1;37m You Traveled :", Miles_Traveled," Miles")
        print("  ")
        print(" \033[1;31m GAME OVER")
        print(" \033[1;37m  ")

        done = True
    # Engine is overheating
    if not done and Engine_Heat_Level >= 5:
        print(" \033[1;37m  ")
        print(" \033[1;33m Your Engine is overheating.")
        print(" \033[1;37m  ")
    # Engine failure
    if not done and Engine_Heat_Level >= 8:
        print(" \033[1;37m  ")
        print(" \033[1;31m Your engine has failed immobilizing your motorcycle.")
        print(" \033[1;37m  ")
        print("\033[1;37m You Traveled :", Miles_Traveled, " Miles")
        print("  ")
        print(" \033[1;31m GAME OVER ")
        print(" \033[1;37m  ")
        done = True
    # Death by zombie hoard
    if not done and Zombie_Distance >= Miles_Traveled:
        print(" \033[1;37m  ")
        print(" \033[1;31m The zombies have caught up to you.")
        print(" \033[1;37m ")
        print("\033[1;37m You Traveled :", Miles_Traveled, " Miles")
        print("  ")
        print(" \033[1;31m GAME OVER")
        print(" \033[1;37m ")
        # zombies are close
        done = True
    elif Zombie_Distance <= 15:
        print(" \033[1;37m ")
        print(" \033[1;33m The zombies are close.")
        print(" \033[1;37m ")
    elif Zombie_Distance <=10:
        if not done and Catch_Disease == 1:
            print(" \033[1;37m ")
            print(" \033[1;31m The zombie hoard is two close you've caught the virus. ")
            print(" \033[1;37m ")
            print("\033[1;37m You Traveled :", Miles_Traveled, " Miles")
            print("  ")
            print(" \033[1;31m GAME OVER ")
            print(" \033[1;37m ")
            done = True
    #when won
    if Miles_Traveled >= 200:
        print(" \033[1;37m ")
        print(" \033[1;32m    Congradulations! You've successfully escaped the "
              " Quarantine Zone after traveling",Miles_Traveled," Miles "
              " in ",Days,"Days. The current date is August ",date,", 2026"
              " You've officially survived the zombie apocalypse.  ")
        print(" \033[1;37m ")
        print(" \033[1;32m YOU'VE BEATEN QUARANTINED ESCAPE.")
        done = True










