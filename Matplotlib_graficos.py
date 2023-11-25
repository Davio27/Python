# A biblioteca Matplotlib cria código que vai gerar um gráfico com os valores de x no eixo xe os valores de y no eixo y, 
# representados por uma linha. Você pode personalizar o gráfico adicionando títulos, 
# rótulos de eixos, legendas, cores, etc. de acordo com suas necessidades.

import matplotlib.pyplot as plt

# Defina os dados que serão plotados
x = [1, 6, 7, 12, 20]
y = [0, 3, 5, 3, 9]

# Crie o gráfico de linha
plt.plot(x, y)

# Adicione rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicione um título
plt.title('Meu Gráfico')

# Exiba o gráfico
plt.show()









