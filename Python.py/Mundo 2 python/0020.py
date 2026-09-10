
contagem=0
maior=0
menor=0
for ask in range(1,6):
    peso=float(input('Peso do {}º indivíduo em kg?:'.format(ask)))
    if ask==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('''O maior peso lido foi de {}kg\nO menor peso lido foi de {}kg'''.format(maior,menor))