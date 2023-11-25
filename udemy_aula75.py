
# # OBS: append é um parâmetro usando para adicionar um valor 
# # recebido de uma variável dentro de outra variável, montando assim uma lista, tupla ou dicionary

# # Criar Função 
# def listaNomes(*nomes):
#     for x in nomes:
#         print(x)
        
        
# # Entrada de quantidade de funcionário
# qdfun = int(input("Digite a quantidade de funcionários: "))

# # criar lista de funcionários
# nomes_fun = []

# # criar loop para digitar o nome dos funcionários 
# for i in range(qdfun):
#     x = input("Digite o nome do funcionário: ")
#     nomes_fun.append(x)
    
# # Imprimir o nome dos funcionários
# listaNomes(*nomes_fun)


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.title('Meu Gráfico')

background_img = mpimg.imread('C:\\Users\\davic\\OneDrive\\Documentos\\main project\\examples\\bg_gradient.jpg')

fig, ax = plt.subplots()

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

ax.imshow(background_img, aspect='auto', extent=(0, 1, 0, 1), zorder=-1)
plt.show()
# Plote seus dados normalmente