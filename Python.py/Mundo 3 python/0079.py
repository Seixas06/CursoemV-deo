listan=[] 
while True:
    valor=int(input('Digite um valor: '))
    listan.append(valor)
    print('Valor adicionado com sucesso...')
    quant=listan.count(valor)
    if quant>1:
        listan.pop()
        print('Valor duplicado! Não vou adicionar...')
    continuar=input('Quer continuar? [S/N] ')[0].strip().upper()
    if continuar=='N':
        break
print('=-'*20)
listan.sort()
print(f'Você digitou os valores {listan}')