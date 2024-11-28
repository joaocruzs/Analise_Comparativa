# Disponível em https://www.geeksforgeeks.org/python-program-for-selection-sort/

import time
import statistics

def selectionSort(array):
    
    size = len(array)
    
    for i in range(size):
        min_index = i

        if (i%1000 == 0):
            print(f'Executando {i}')
        
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
         
        (array[i], array[min_index]) = (array[min_index], array[i])

if __name__ == '__main__':

        nomeArquivo=input("Digite o nome do arquivo: ")
      
        historico_tempo = []
        for i in range(5):
            with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.time()*1000 #ms
            selectionSort(valoresInt)
            fim = time.time()*1000

            timer = (fim - inicio)
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ms')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ms')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ms')