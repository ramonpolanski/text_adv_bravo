from stringcolor import cs
import time
import os
tresure = 0
varActTwo = "/text_adv_bravo_act_3.py"
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def gameOver():
    time.sleep(1)
    printc("You Died!", "red")
    time.sleep(2)
    printc("y | n", "blue")
    decision = input("Try again?: ")
    if decision.lower() == "y":
        clear_console()
    elif decision.lower() == "n":
        clear_console()

def actTwo():
    exec(open("./text_adv_bravo_act_2.py").read())
def actThree():
    exec(open("./text_adv_bravo_act_3.py").read())

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    printc("Restarting..", "white")
    time.sleep(1)
    printc("Restarting..", "yellow")
    time.sleep(1)
    printc("Restarting..", "green")
    time.sleep(1)
    printc("10%", "red")
    time.sleep(1)
    printc("80%", "red")
    time.sleep(1)
    printc("99%", "red")
    time.sleep(3)
    printc("That were.... lies :D", "white")





intro= "Introduction:"
printc(intro, "green")
printc("You find yourself washed ashore on a mysterious island after a violent storm wreaks havoc on your ship. As you regain consciousness, you realize you're not alone. Pirate remnants litter the beach, and the distant sounds of waves crashing against the rocky cliffs echo ominously. Determined to survive, you venture deeper into the island's uncharted territory, unaware of the dangers lurking within.")
time.sleep(4)
printc("Act 1: The Encounter", "green")
printc("As you explore the island, you stumble upon a ragtag group of pirates who have made this island their hideout. They greet you with suspicion, questioning your motives. With no means of escape, you strike a deal with the pirates: help them locate a legendary treasure rumored to be hidden somewhere on the island, and they'll assist you in returning home.")
printc("fight | help | negotiate", "blue")
decision = input("Choose: ")
if decision.lower() == "fight":
    gameOver()
    
elif decision.lower() == "help":
    printc("You are helping the pirates and agree to their conditions")
    time.sleep(3)
    actTwo()
    
elif decision.lower() == "negotiate":
    printc("You tell the pirates that you will help them if they give you a part of the tresure")
    time.sleep(2)
    printc('"Pirate" How much do you want?')
    decision = int(input("Enter a percentage: "))
    if decision <= 33:
        tresure += 1
        print(tresure)
        actTwo()
    elif decision > 33:
        gameOver()



    