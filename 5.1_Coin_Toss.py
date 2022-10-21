'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random

#variables
heads = 0
tails = 0
cointoss = 0
coinresult = random.randint(1,2)
#loop
while True:
    cointoss +=1

    # end if
    if cointoss > 100:
        break
    if coinresult == 1:
        heads +=1
        cointoss +=1
    elif coinresult == 2:
        tails +=1
        cointoss +=1
print("Heads came up", heads, "times")
print("Tails came up", tails, "times")










