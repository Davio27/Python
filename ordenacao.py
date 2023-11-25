def ordenacao_por_insercao(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# Exemplo de uso:
lista = [12, 11, 13, 5, 6, 1, 9, 20, 45, 3, 7, 18]
ordenacao_por_insercao(lista)
print("Lista ordenada:", lista)