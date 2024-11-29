from createArray import createArray
import time
import statistics

def countingSort(arr, exp1): 

	n = len(arr) 
	output = [0] * (n) 
	count = [0] * (10) 
	
	for i in range(0, n): 
		index = (arr[i]/exp1) 
		count[int((index)%10)] += 1

	for i in range(1,10): 
		count[i] += count[i-1] 

	i = n-1
	while i>=0: 
		index = (arr[i]/exp1) 
		output[ count[ int((index)%10) ] - 1] = arr[i] 
		count[int((index)%10)] -= 1
		i -= 1

	i = 0
	for i in range(0,len(arr)): 
		arr[i] = output[i] 

def radixSort(arr):

	max1 = max(arr)

	exp = 1
	while max1 // exp > 0:
		countingSort(arr,exp)
		exp *= 10

if __name__ == '__main__':

        size=int(input("Digite o tamanho do arquivo: "))
      
        historico_tempo = []
        for i in range(5):
            createArray(size)
            with open('entrada', 'r', encoding='utf-8') as arquivo:
                valores=arquivo.read().split()
                valoresInt = [int(valor) for valor in valores]
            inicio = time.perf_counter()
            radixSort(valoresInt)
            fim = time.perf_counter()

            timer = (fim - inicio)* 1e6
            historico_tempo.append(timer)

        for i, tempo in enumerate(historico_tempo):
            print(f'Execução {i+1}: {tempo:.2f}ns')

        media = sum(historico_tempo) / 5
        desvio_padrao = statistics.stdev(historico_tempo)
        print(f'Tempo Médio: {media:.2f}ns')
        print(f'Desvio Padrão: {desvio_padrao:.2f}ns')
