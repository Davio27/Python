import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Carregue a imagem de fundo
background_image = mpimg.imread('C:\\Users\\davic\\OneDrive\\Documentos\\main project\\examples\\bg_gradient.jpg')

# Crie dados de exemplo para o gráfico
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Crie uma figura e um eixo
fig, ax = plt.subplots()

# Exiba a imagem de fundo no gráfico
ax.imshow(background_image, aspect='auto', extent=(min(x), max(x), min(y), max(y)))

# Plote o gráfico
ax.plot(x, y, 'r')

# Mostre o gráfico
plt.show()