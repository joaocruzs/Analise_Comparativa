import random  

def createArray(nome_arquivo,size):
    with open(nome_arquivo,'w') as arquivo:
        for _ in range(size):
            valor=str(random.randint(0,size*2))
            arquivo.write(valor + " ")
        

#criando os vetores para 500, 1000, 5000
createArray('500.txt',500)
createArray('1k.txt',1000)
createArray('5k.txt',5000)

#criando os vetores para 30k, 80k, 100k
createArray('30k.txt',30000)
createArray('80k.txt',80000)
createArray('100k.txt',100000)

#criando os vetores para 150k, 200k
createArray('150k.txt',150000)
createArray('200k.txt',200000)
