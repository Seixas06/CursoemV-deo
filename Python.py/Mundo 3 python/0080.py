numbers=list()
for p in range(0,6):
    valor=int(input('Digite um valor: '))
    if p==0 or valor>numbers[-1]:
        numbers.append(valor)
        print('Adicionado ao final da lista')
    else:
        pos=0
        while pos<len(numbers):
            if valor <= numbers[pos]:
                numbers.insert(pos,valor)
                print(f'Adicionado na posição {pos}')
                break
            pos+=1
print('-='*30)
print(f'Os valores digirtados em ordem foram {numbers}')