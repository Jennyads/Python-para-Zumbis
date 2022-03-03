contador = 0

for x in range (1067, 3628):
    if not x%2 and not x%7:
        contador = contador + 1

print(contador)
