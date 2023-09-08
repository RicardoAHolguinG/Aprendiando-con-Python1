print("$$$$$$$$$$$$$$$$$$$$$$$$")
print("Numero mayor entre los 3")
print("$$$$$$$$$$$$$$$$$$$$$$$$ \n")

import time

Nombre = input("Escriba su nombre: ")
Num1 = int(input("Escribe el primer numero: "))
Num2 = int(input("Escribe el segundo numero: "))
Num3 = int(input("Escribe el tercer numero: "))
time.sleep(1)

if Num1 > Num2 and Num1 > Num3:
    print("Este numero ", Num1 ," es mayor entre los 3.")

else:
    if Num2 > Num3:
        print("Este numero ", Num2 ," es mayor entre los 3.")
        
    else:
        print("Este numero ",Num3 ," es mayor entre los 3.")
time.sleep(1)

print()
print("Buenas tardes.", Nombre)
    
    