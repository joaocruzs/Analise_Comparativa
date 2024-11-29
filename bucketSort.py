import time
import statistics
from insertionSort import insertionSort
from createArray import createArray

def bucketSort(arr):
    n= len(arr)

    if n <= 1:
        return 
    
    valorMaximo=max(arr)
    valorMinimo=min(arr)

    intervalo=(valorMaximo-valorMinimo)/n

    buckets=[[] for _ in range(n)]

    for num in arr:
        index= int((num-valorMinimo)/intervalo)

        if index==n:
            index-=1

        buckets[index].append(num)

    for bucket in buckets:
        insertionSort(bucket)
        
    i= 0
    for bucket in buckets:
        for num in bucket:
            arr[i]=num
            i+=1


if __name__ == '__main__':

        size=int(input("Digite o tamanho do arquivo: "))
      
        historico_tempo = []
        for i in range(5):
            createArray(size)
            with open('entrada', 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.perf_counter()
            bucketSort(valoresInt)
            fim = time.perf_counter()

            timer = (fim - inicio)* 1e6
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ns')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ns')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ns')
