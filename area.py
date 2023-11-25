# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

# Entrada
# O arquivo de entrada contém três valores com um dígito após o ponto decimal.

# Saída
# O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, 
# sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.



a = float(input())
b = float(input())
c = float(input())
triangulo = round((a*c)/2,3)
circulo = round(3.14159*(c*c),3)
trapezio = round(((a+b)*c)/2,3)
quadrado = round(b*b,3)
retangulo = round(a*b,3)

print(f"triangulo: {triangulo}")
print(f"circulo: {circulo}")
print(f"trapezio: {trapezio}")
print(f"quadrado: {quadrado}")
print(f"retangulo: {retangulo}")