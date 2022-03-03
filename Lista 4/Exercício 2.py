
import random
valores = random.sample(range(100),20)
print(valores)

par = []
impar = []

for x in valores:
    if x % 2 ==0:
        par.append(x)
    
    else:
        impar.append(x)

par.sort()
impar.sort()
print('Par', par)
print('Ímpar', impar)
