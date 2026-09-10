numeros=list()
pares=list()
impares=list()
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar=str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar=='N':
        break
for p in numeros:
    if p%2==0:
        pares.append(p)
    else:
        impares.append(p)
print('=-'*30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')