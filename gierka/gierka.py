from playsound import playsound
from pyfiglet import Figlet
import random

health = 100

def welcome():
    print("Witaj mimiku! Jesteś potworem o wyglądzie skrzyni, który zjada ludzi. W swoim życiu musisz podjąć decyzje czy zjeść człowieka, ukryć się i oddać skarby albo uciec narażając się na pościg lub wykrycie.")
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

    
def secondStage(health):
    print("Zbliża się do Ciebie Palladyn ubarany w błyszczącą zbroje,  wyposażony w magiczny, dwuręczny miecz, który dzierży w 1 ręce. Do tego widzisz tarcze w jaego drugiej ręce.  Jaką decyzje podejmiesz?")
    playerChoice = int(input("1. Walcz\t2. Uciekaj\t3. Oddaj skarby: "))
    if playerChoice == 1:
        print("Podejmujesz walkę, ale z marnym skutkiem. Giniesz!")
        endGame()

    elif playerChoice == 2:
        print("Próbujesz uciekać")
        generate = random.randint(1,2)
        if generate == 1:
            print("Palladyn cię dogania, tracisz 99HP")
            health -= 99
        else:
            print("Udaje ci się uciec!")

        healthInfoMessage(health)
        
    elif playerChoice == 3:
        print("Udaje Ci się przekonać wroga do wzięcia łapówki")
        healthInfoMessage(health)

    else:
        wrongChoiceMessage()
#---------STAGES---------#
def healthInfoMessage(health):
    print("Twoje punkty zdrowia:", health)

def wrongChoiceMessage():
    dialogOptions = ["Nie kombinuj!", "Nie masz innych opcji!", "Ciekawość może zabić!"]
    print(random.choice(dialogOptions))

def endGame():
    pass

def main():
    welcome()
    secondStage(health)

main()