import random  

def createArray(size):
    with open('entrada','w') as arquivo:
        for _ in range(size):
            valor=str(random.randint(0,size*2))
            arquivo.write(valor + " ")
        


