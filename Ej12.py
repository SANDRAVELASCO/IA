import random
# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Pedir al usuario que adivine el número
adivina = int(input("Adivina un número entre 1 y 10: "))

# Verificar si el usuario acertó
if adivina == numero_aleatorio:
    print("¡Correcto! Has adivinado el número.")
else:
    print(f"Incorrecto, el número era {numero_aleatorio}.")
