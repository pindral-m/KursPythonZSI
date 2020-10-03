from playsound import playsound
from pyfiglet import Figlet
import random
import sys

health = 100

def welcome():
    print("Witaj mimiku! Jesteś potworem o wyglądzie skrzyni, który zjada ludzi. W swoim życiu musisz podjąć decyzje czy zjeść człowieka, ukryć się i oddać skarby albo uciec narażając się na pościg lub wykrycie.")
    #playsound("")

#---------STAGES---------#
def firstStage(health):
    print("Obok Ciebie przechodzi wieśniak uzbrojony w widły. Co robisz?")
    playerChoice = int(input("1. Zwróć na siebie uwagę\t2. Schowaj się: "))
    if playerChoice == 1:
        playerChoice = int(input("Pomyślnie przyciągasz uwagę wieśniaka. Co chcesz zrobić?\n1. Zjedz go\t2. Oddaj skarby: "))

        if playerChoice == 1:
            print("Zjadasz wieśniaka i zyskujesz 10HP")
            health += 10
            healthInfoMessage(health)

        elif playerChoice == 2:
            print("Oddałeś skarby wieśniakowi. Tracisz 5HP!")
            health -= 5
            healthInfoMessage(health)

    elif playerChoice == 2:
        print("Chowasz się i czekasz na następną ofiarę")

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

def thirdStage(health):
    print("Podchodzi do Ciebie dwu osobowy zespół złożony z wojownika i uzdrowiciela. Twój wybór: ")
    playerChoice = int(input("1. Walcz\t2. Oddaj skarby\t3. Uciekaj: "))
    if playerChoice == 1:
        print("Kogo chcesz zaatakować?")
        playerChoice = int(input("1. Wojownika\t2. Uzdrowiciela"))
        if playerChoice == 1:
            print("Podejmujesz walkę z wojownikiem, który jest leczony przez uzdrowiciela. Tracisz 50HP")
            health -= 50
            healthInfoMessage(health)

        elif playerChoice == 2:
            print("Uzdrowiciel ginie. Wojownik sam nie daje rady po walce z tobą ginie. Zjadasz obydwa trupy")
            health += 25
            healthInfoMessage(health)

        else:
            wrongChoiceMessage()

    elif playerChoice == 2:
        print("Udaje Ci się przekonać wroga do wzięcia łapówki")

    elif playerChoice == 3:
        print("Próbujesz uciekać")
        generate = random.randint(1,2)
        if generate == 1:
            print("Udaje Ci się uciec!")

        else:
            print("Nrogowie Cię gonią! Co chcesz zrobić?")
            playerChoice = int(input("1. Walcz\t2. Uciekaj: "))
       
    else:
        wrongChoiceMessage()
#---------STAGES---------#
def healthInfoMessage(health):
    print("Twoje punkty zdrowia:", health)

def wrongChoiceMessage():
    dialogOptions = ["Nie kombinuj!", "Nie masz innych opcji!", "Ciekawość może zabić!"]
    print(random.choice(dialogOptions))

def endGame():
    sys.exit()

def main():
    welcome()
    firstStage(health)
    secondStage(health)
    thirdStage(health)

main()