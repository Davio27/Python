import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Carregue a imagem do arquivo
img = mpimg.imread('C:\\Users\\davic\\OneDrive\\Documentos\\main project\\examples\\bg_gradient.jpg')

# Exiba a imagem em segundo plano
plt.imshow(img, extent=[0, 5, 0, 5], aspect='auto')

# Trace um gráfico de exemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
plt.plot(x, y, 'ro--')

# Adicione um título ao gráfico
plt.title('Exemplo de gráfico com imagem de plano de fundo')

# Exiba o gráfico
plt.show()





