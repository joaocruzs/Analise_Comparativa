import time
import statistics

def countSort(arr):
 
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
 
    for i in arr:
        count[i] += 1
 
    for i in range(1, len(count)):
        count[i] += count[i-1]
 
    for i in reversed(arr):
        output[count[i]-1] = i
        count[i] -= 1

    return output 

if __name__ == '__main__':

        nomeArquivo=input("Digite o nome do arquivo: ")
      
        historico_tempo = []
        for i in range(5):
            with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.time()*1000000 #ns
            countSort(valoresInt)
            fim = time.time()*1000000

            timer = (fim - inicio)
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ns')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ns')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ns')