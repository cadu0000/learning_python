vetor_par = []
vetor_impar = []
total_par = 0
total_impar = 0

for n in range(348, 863):
    if n % 2 == 0:
        vetor_par.append(n)
    else:
        vetor_impar.append(n)

print(vetor_par)
print(vetor_impar)

for n in range(vetor_par):
    total_par += n
for n in range(vetor_impar):
    total_impar += n
print(total_par)
print(total_impar)