dividendo = -1
divisor= -1

while (dividendo <= 0 or divisor <= 0):
    dividendo = int(input("Digite el dividendo: "))
    divisor = int(input("Digite el divisor: "))

    if (dividendo <= 0 or divisor <= 0):
        print ("Error. Solo numeros positivos")

while(dividendo >= divisor):
    dividendo -= divisor

print(dividendo)
