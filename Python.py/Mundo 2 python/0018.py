palavra=str(input('Escreva a sua palavra: ')).replace(' ','').lower()
inverso=''
for letra in range(len(palavra)-1,-1,-1):
    inverso+=palavra[letra]
print(palavra,' = ',inverso)
if inverso==palavra:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')