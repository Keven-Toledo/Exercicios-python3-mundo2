soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont = cont + 1
        soma = soma + numero
print(f'A soma de todos os {cont} valores é {soma}')
