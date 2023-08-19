print("$$$$$$$$$$$$$$$$$$$")
print("Generator Password.")
print("$$$$$$$$$$$$$$$$$$$ \n")

import random 


BigWords = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SmallWords = "abcdefghijklmnopqrstuvwxyz"
Numbers = "123456789"
Simbols = "!$%&/()=?¿Ñ¨¨:;.,-/*-@"

All = (BigWords + SmallWords + Numbers + Simbols)
Length = 15

Passwords = "".join(random.sample(All, Length))

print(Passwords)