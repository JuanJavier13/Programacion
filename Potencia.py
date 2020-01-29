base = -1
potencia = -1

while (base <= 0 or potencia <= 0):
    base = int(input("Digite una base: "))
    potencia = int(input("Digite una potencia: "))

    if (base <= 0 or potencia <= 0):
        print ("Error. Solo numeros positivos")

acumulador = base

while (potencia > 1):
    base *= acumulador
    potencia -= 1

print (base)
