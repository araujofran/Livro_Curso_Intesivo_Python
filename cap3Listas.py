import time

lista =[ 'A',  'B' , 'C']
lista.insert(3,'D')
tam=len(lista)
print (tam*'~~')
print ('Usando o comando insert')
for i,p in enumerate(lista):
    print(f'Na posição {i} temos o {p}',flush=True)
    time.sleep(1)
del lista[0]
print (tam*'~~')
print ('Usando o comando del')
for i,p in enumerate(lista):  
    print(f'Na posição {i} temos o {p}',flush=True)
    time.sleep(1)
print (tam*'~~')
print ('pop() apaga o ultimo item')
lista.pop()
print(lista)
print ('reverse() inverte os itens na lista')
lista.reverse()
print(lista)
print (len(lista))


