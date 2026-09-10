list=[]
while True:
    list.append(int(input('Digite um número: ')))
    continuar=input('Quer continuar? [S/N]: ').strip().upper()[0]
    if continuar=='N':
        break
print('=-'*30)
list.sort(reverse=True)
print(f'Você digitou {len(list)} elementos.')
print(f'Os valores em ordem decrescente são {list}')
if 5 in list:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista')
