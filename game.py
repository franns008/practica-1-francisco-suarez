from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-","*","/"]
times = 5
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
correcto=0
incorrecto=0
for i in range(0, times):
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    while (operator=="/" and number_2==0):
        number_2 = randrange(10)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    result = int(input("resultado: "))
    match operator:
        case "+":
            x=number_1+number_2
        case "-":
            x=number_1-number_2
        case "*":
            x=number_1*number_2
        case"/":
            x=number_1//number_2
    print (x)
    if (x==result):
        print ("El resultado fue correcto")
        correcto=correcto+1
    else:
        print("el resultado fue incorrecto")
        incorrecto=incorrecto+1
    end_time = datetime.now()
    total_time = end_time - init_time
    print(f"\n Tardaste {total_time.seconds} segundos.")
print("cantidad de respuestas correctas ",{correcto})
print("cantidad de respuestas incorrectas ", {incorrecto})