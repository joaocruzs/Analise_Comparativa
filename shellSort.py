# Disponível em https://www.geeksforgeeks.org/python-program-for-shellsort/

import time
import statistics

def shellSort(arr):
 
    n = len(arr)
    gap = n//2
 
    while gap > 0:
 
        for i in range(gap,n):
            temp = arr[i]

            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
 
            arr[j] = temp
        gap //= 2
 

if __name__ == '__main__':

        nomeArquivo=input("Digite o nome do arquivo: ")
      
        historico_tempo = []
        for i in range(5):
            with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.time()*1000000 #ns
            shellSort(valoresInt)
            fim = time.time()*1000000

            timer = (fim - inicio)
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ns')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ns')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ns')
        