#Faça um programa que crie dois vetores com
#10 elementos aleatórios entre 1 e 100

import random

vetor1 = random.sample(range(100),10)
vetor2 =random.sample(range(100),10)
vetor3 = []

x = 0
while x <10:
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[x])
    x = x + 1

print('Esse é o vetor 1: ',vetor1)
print('Esse é o vetor 2: ',vetor2)
print('Esse é o vetor 3: ',vetor3)



ou

import random

vetor1 = random.sample(range(100),10)
vetor2 =random.sample(range(100),10)
vetor3 = []

for k in range(len(vetor1)):
    vetor3.append(vetor1[k])
    vetor3.append(vetor2[k])

print('Esse é o vetor 1: ',vetor1)
print('Esse é o vetor 2: ',vetor2)
print('Esse é o vetor 3: ',vetor3)

ou

v3 = []
for x, y in zip(v1, v2): v3.extend([x,y])
print(v1)
print(v2)
print(v3)
