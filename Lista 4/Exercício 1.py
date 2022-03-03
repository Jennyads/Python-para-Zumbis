import random
valores = random.sample(range(100),10)
print(valores)

maior = valores[0]
menor = valores[0]

for x in valores:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
        
print('Maior:', maior)
print('Menor:', menor)


ou

while k < len(v):
	x=v[k]
	if x < menor:
		menor = x
	if x > maior:
		maior = x
	k = k + 1
