'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

print("  Welcome to Quarantined Escape The current date is August 2nd, 2026. /n"
      " Two days ago the World ended after a modified and highly contagious strand /n"
      " of the Ophiocordyceps Unilateralis fungus or Zombie Ant fungus was released /n"
      " from a lab in Washington near the west coast, turning anyone that comes into/n"
      " contact with it into a violent enraged zombie.  ")
print(" ")
print("     Right before the electrical grid was shut down the government was able to /n"
      " send out a map of washington and where they would be enacting a quarantine-zone. /n"
      " your job is to travel 200 miles in order to escape from the quarantine zone before /n"
      " they shut the state off from the rest of the world. ")
print(" ")
print("     You will start off with 5 drinks in your canteen and there is a 1 in 20 chance of /n"
      " You finding a Convenience Store. You can type E for your Status./n"
      " good luck and may god be with you.")
print(" ")
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

    answer = input( "What steps would you like to take in order to survive.")
    # Option Q for quit
    if answer.upper() == ("Q"):
        done = True
        print("  ")
        print(" GAME OVER! ")
        print("  ")
    elif answer.upper() == ("E"):
        print("  ")
        print( "Miles Traveled:",Miles_Traveled)
        print( "Drinks in Canteen:",Canteen_Drinks)
        print( "The zombies are currently",Zombie_Distance*-1, "Miles Behind you.")
        print("  ")
    # option D for stop for the night
    elif answer.upper() == ("D"):
        Engine_Heat_Level = 0
        date += 1
        Days += 1
        Zombie_Distance += random.randrange(7, 15)
        print("  ")
        print(" The engine in your motorcycle has cooled down!")
        print("  ")
    # option C for move ahead at full speed
    elif answer.upper() == ("C"):
        if Store == 1:
            print("  ")
            print("Wow you've discovered a Convenience Store!")
            print("  ")
            Engine_Heat_Level = 0
            Thirst = 0
            Canteen_Drinks = 5
        else:
            Miles_Traveled += random.randint(10, 20)
            Thirst += 1
            Engine_Heat_Level += random.randrange(1, 4)
            Zombie_Distance += random.randrange(7, 15)
    # Option B for move ahead at a moderate speed
    elif answer.upper() == ("B"):
        if Store == 1:
            print("  ")
            print("Wow you've discovered a Convenience Store!")
            print("  ")
            Engine_Heat_Level = 0
            Thirst = 0
            Canteen_Drinks = 5
        else:
            Miles_Traveled += random.randint(5, 12)
            Thirst += 1
            Engine_Heat_Level += 1
            Zombie_Distance += random.randrange(7, 15)
    # Option A for Drink from canteen
    elif answer.upper() == ("A"):
        Canteen_Drinks -= 1
        Thirst -= 1
        if Canteen_Drinks == 0:
            print("  ")
            print(" Your canteen has no more water in it.")
            print("  ")
    # thirsty
    if not done and Thirst >= 4:
        print("  ")
        print(" You are thirsty.")
        print("  ")
    # Death by thirst
    if not done and Thirst >= 6:
        print("  ")
        print(" You have died of thirst")
        print("  ")
        print(" GAME OVER")
        print("  ")
        done = True
    # Engine is overheating
    if not done and Engine_Heat_Level >= 5:
        print("  ")
        print(" Your Engine is overheating.")
        print("  ")
    # Engine failure
    if not done and Engine_Heat_Level >= 8:
        print("  ")
        print(" Your engine has failed immobilizing your motorcycle.")
        print("  ")
        print(" GAME OVER ")
        print("  ")
        done = True
    # Death by zombie hoard
    if not done and Zombie_Distance >= Miles_Traveled:
        print("  ")
        print(" The zombies have caught up to you.")
        print("  ")
        print(" GAME OVER")
        print("  ")
        # zombies are close
        done = True
    elif Zombie_Distance <= 15:
        print("  ")
        print(" The zombies are close.")
        print("  ")
    elif Zombie_Distance <=10:
        if not done and Catch_Disease == 1:
            print(" ")
            print(" The zombie hoard is two close you've caught the virus. ")
            print(" ")
            print(" GAME OVER ")
            done = True
    #when won
    if Miles_Traveled >= 200:
        print("  ")
        print("     Congradulations! You've successfully escaped the /n"
              " Quarantine Zone after traveling",Miles_Traveled," Miles /n"
              " in ",Days,"Days. The current date is August ",date,", 2026"
              " You've officially survived the zombie apocalypse.  ")
        print("  ")
        print(" YOU'VE BEATEN QUARANTINED ESCAPE.")
        done = True










