
import time

print("$$$$$$$$$$$$$$$$4$$$$$$$$$$")
print("Calculadora de una variable.")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$ \n")

time.sleep(2)

Name = input("Escriba su nombre: ")

print(Name,",escriba la opcion deseada.")
time.sleep(1)

print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACION")
print("4. DIVICION")
print("5. MODULO O RESTO \n")

Number = int(input("Escriba una de las 5 opciones: "))
print()
time.sleep(1)

if Number == 1:
    print("Elegiste suma.")
    Number = int(input("Escriba el primer Numero: "))
    Number += int(input("Escriba el segundo numero: "))
    print("El resultado de su suma es:", Number)

elif Number == 2:
    print("Elegiste resta.")
    Number = int(input("Escriba el primer Numero: "))
    Number -= int(input("Escriba el segundo numero: "))
    print("El resultado de su resta es:", Number)

elif Number == 3:
    print("Elegiste Multiplicacion.")
    Number = int(input("Escriba el primer Numero: "))
    Number *= int(input("Escriba el segundo numero: "))
    print("El resultado de su multiplicacion es:", Number)
    
elif Number == 4:
    print("Elegiste Divicion.")
    Number = int(input("Escriba el primer Numero: "))
    Number /= int(input("Escriba el segundo numero: "))
    print("El resultado de su divicion es:", Number)

elif Number == 5:
    print("Elegiste Modulo o Resto.")
    Number = int(input("Escriba el primer Numero: "))
    Number %= int(input("Escriba el segundo numero: "))
    print("El resultado de su modulo o resto es:", Number)

else:
    print("Opcion no contemplada, intentelo de nuevo.")

print()
time.sleep(2)
print(Name,", Buenas Noches.")

    