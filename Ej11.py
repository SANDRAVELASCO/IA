# Solicitar al usuario que ingrese un número
num = float(input("Ingresa un número: "))

# Verificar si el número es positivo, negativo o cero
if num > 0:
    print(f"{num} es un número positivo.")
elif num < 0:
    print(f"{num} es un número negativo.")
else:
    print(f"{num} es igual a cero.")
