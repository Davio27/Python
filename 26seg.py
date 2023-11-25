mult = int(input("Digite o multiplicando"))
multdor = int(input("Digite o multiplicador"))
resultado = 0
for x in range(1, multdor+1):
    resultado=resultado + mult

print(mult, "x", multdor, "=", resultado)

dividendo = int(input("Digite o dividendo"))
divisor = int(input("Digite o divisor"))
resto = dividendo
quociente=0

while resto >= divisor:
    resto = resto - divisor
    quociente = quociente +1

print(dividendo, "/", divisor, "=", quociente, " e o resto = ", resto)