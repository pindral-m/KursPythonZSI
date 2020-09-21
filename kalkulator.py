print("***The best calculator ever!***")
usrInput = input("Wprowadź działanie: ")
x = ''
y = []

for i in usrInput:
    if i == '+' or i == '-' or i == '/' or i == '*':
        y.append(float(x))
        x=''
        z = i
    else:
        x += i

y.append(float(x))

if z == '+':
    print(usrInput, "=", y[0]+y[1])
elif z == '-':
     print(usrInput, "=", y[0]-y[1])
elif z == '/':
    if y[1] == 0:
        print("Nie dzielimy przez 0!")
    else:
        print(usrInput, "=", y[0]/y[1])
elif z == '*':
     print(usrInput, "=", y[0]*y[1])
else:
    print("Błędne działanie!")
