# Capitulo 4
import time
lista=['A','B','C','D']

for p,l in enumerate(lista):
    if p<len(lista):
        print (l,flush=True,end=' ')
        time.sleep(0.8)
    
print('.')
print('\n')
squares = [value**2 for value in range(1,11)]
print(squares)
    