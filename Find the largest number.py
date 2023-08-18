print("$$$$$$$$$$$$$$$$$$$")
print("Find the largest number")
print("$$$$$$$$$$$$$$$$$$$ \n")

Num1= int(input("Write the first number: "))
Num2= int(input("Write the second number: "))
Num3= int(input("Write the third number: "))

if Num1 > Num2 and Num1 > Num3:
    print("The number ",Num1," is greater among the others.")

else:
    
    if Num2 > Num3:
        print("The number ",Num2," is greater among the others.")
        
    else:
        print("The number ",Num3," is greater among the others.")


print()
print("You are the best.")