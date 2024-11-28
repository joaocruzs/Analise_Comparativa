# Disponível em https://www.geeksforgeeks.org/python-program-for-insertion-sort/?ref=lbp

import time
import statistics

def insertionSort(arr):
    n = len(arr)  

    if n <= 1:
        return
 
    for i in range(1, n):  
        key = arr[i]  
        j = i-1
        
        if (i%1000 == 0):
            print(f'Executando {i}')
            
        while j >= 0 and key < arr[j]:  
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 
 


if __name__ == '__main__':

        nomeArquivo=input("Digite o nome do arquivo: ")
      
        historico_tempo = []
        for i in range(5):
            with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.time()*1000 #ms
            insertionSort(valoresInt)
            fim = time.time()*1000

            timer = (fim - inicio)
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ms')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ms')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ms')