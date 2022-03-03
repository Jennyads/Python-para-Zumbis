habitantesA = 80000
habitantesB = 200000
ano = 0
while habitantesA <= habitantesB:
    habitantesA = habitantesA * 0.03 + habitantesA
    habitantesB = habitantesB * 0.015 + habitantesB
    ano = ano + 1
print('Ano', ano)
