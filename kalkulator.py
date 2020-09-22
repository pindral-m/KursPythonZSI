import sys

print("***The best calculator ever!***")
while True:
    try:
        usrInput = input("\nWprowadź działanie w formacie x+y lub x*y etc\nJeżeli chcesz zakończyć wciśnij Ctrl + C:\n")
        valueToConvert = ''
        convertedValues = []
        charCounter = 0

        for i in usrInput:
            if (i == '+' or i == '-' or i == '/' or i == '*') and (charCounter < 2):
                charCounter+=1
                try:
                    convertedValues.append(float(valueToConvert))
                except ValueError:
                    valueToConvert += i
                    continue

                valueToConvert += i
                valueToConvert = ''
                z = i
            else:
                valueToConvert += i
        try:
            convertedValues.append(float(valueToConvert))
        except ValueError:
            print("Błędna wartość!")
            continue


        if len(convertedValues) == 1:
            print(convertedValues[0])
        else:
            if z == '+':
                print(usrInput, "=", convertedValues[0]+convertedValues[1])
            elif z == '-':
                print(usrInput, "=", convertedValues[0]-convertedValues[1])
            elif z == '/':
                if convertedValues[1] == 0:
                    print("Nie dzielimy przez 0!")
                else:
                    print(usrInput, "=", convertedValues[0]/convertedValues[1])
            elif z == '*':
                print(usrInput, "=", convertedValues[0]*convertedValues[1])
            else:
                print("Błędne działanie!")

    except KeyboardInterrupt:
        sys.exit()