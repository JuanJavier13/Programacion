multiplicando = -1
multiplicador = -1

while(multiplicando <= 0 or multiplicador <= 0):
    multiplicando = int(input("Digite un multiplicando: "))
    multiplicador = int(input("Digite un multiplicador: "))

    if(multiplicando <= 0 or multiplicador <= 0):
        print("Error, Solo numeros positivos")

acumulador = multiplicando

while(multiplicador > 1):
    multiplicando = multiplicando + acumulador
    multiplicador = multiplicador - 1

print(multiplicando)
