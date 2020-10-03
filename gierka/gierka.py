from playsound import playsound
from pyfiglet import Figlet
import random

health = 100

def welcome():
    print("Witaj mimiku! Jesteś potworem o wyglądzie skrzyni, który zjada ludzi. W swoim życi musisz podjąć decyzje czy zjeść człowieka, ukryć się i oddać skarby albo uciec narażając się na pościg lub wykrycie.")
    #playsound("")

#---------STAGES---------#
def firstStage(health):
    print("Obok Ciebie przechodzi wieśniak uzbrojony w widły. Co robisz?")
    playerChoice = int(input("1. Zwróć na siebie uwagę\t2. Schowaj się: "))
    if playerChoice == 1:
        playerChoice = int(input("Pomyślnie przyciągasz uwagę wieśniaka. Co chcesz zrobić?\n1. Zjedz go\t2. Oddaj skarby"))

        if playerChoice == 1:
            print("Zjadasz wieśniaka i zyskujesz 10HP")
            health += 10
            healthInfoMessage(health)

        elif playerChoice == 2:
            print("Oddałeś skarby wieśniakowi. Tracisz 5HP!")
            health -= 10
            healthInfoMessage(health)

    elif playerChoice == 2:
        print("Czekasz na następną ofiarę, z głodu tracisz 3 punkty zdrowia.")
        health -= 3
        healthInfoMessage(health)

    else:
        wrongChoiceMessage()

#---------STAGES---------#
def healthInfoMessage(health):
    print("Twoje punkty zdrowia:", health)

def wrongChoiceMessage():
    dialogOptions = ["Nie kombinuj!", "Nie masz innych opcji!", "Ciekawość może zabić!"]
    print(random.choice(dialogOptions))

def main():
    welcome()
    firstStage(health)

main()