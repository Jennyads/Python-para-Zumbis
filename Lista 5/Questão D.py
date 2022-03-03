contador = 0
for x in range(18644, 33087):
    if '2' in str(x) and '7' not in str(x):
        contador = contador + 1

print(contador)
