import math 

# input

X = int(input("digite un numero: "))

#precessing 
if X > 0:
    RTA = "Positivo"
elif X == 0:
    RTA = "su numero es neutro"
else:
    RTA = "negativo"

# output

print("el numero",X, " es " ,RTA)
