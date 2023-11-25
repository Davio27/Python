import math

print("\n")
print("Formula de Baskara")
print("\n")
a = float (input("Digite o valor do termo a: "))
b = float (input("Digite o valor do termo b: "))
c = float (input("Digite o valor do termo c: "))

delta = (b*b) - (4*a*c)

if delta >= 0:
    raiz = math.sqrt(delta)
    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)
    print(f"Delta = {delta}")
    print("Raiz = ", raiz)
    print("X1 = ", x1)
    print("X2 = ", x2)
if x1 != x2:
    print("\n")
    print("X1 e X2 sao raizes reaiz e distintas")

if x1 == x2:
    print("\n")
    print("X1 e X2 sao raizes reais e iguais")

else:
    print("\n")
    print(" A euquacao nao possui raizes reais")
    

