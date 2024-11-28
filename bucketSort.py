import time
import statistics
from insertionSort import insertionSort

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

        nomeArquivo=input("Digite o nome do arquivo: ")
      
        historico_tempo = []
        for i in range(5):
            with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.time()*1000000 #ns
            bucketSort(valoresInt)
            fim = time.time()*1000000

            timer = (fim - inicio)
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ns')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ns')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ns')
