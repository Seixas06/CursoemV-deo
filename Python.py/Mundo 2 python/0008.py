print('-='*9)
print('Vamos calcular IMC')
print('-='*9)
print('Precisarei de sua altura e peso.')
altura=float(input('Digite a altura (m): '))
peso=float(input('Digite o peso (kg): '))
imc=peso/altura**2
print('O seu IMC é {:.2f}.'.format(imc))
if imc<18.5:
    print('\033[1;33Você está abaixo do peso.')
elif imc<25:
    print('\033[1;32mVocê está no peso ideal.')
elif imc<30:
    print('\033[1;33mVocê está com sobrepeso.')
elif imc<40:
    print('\033[1;31mVocê está obeso.')
else:
    print('\033[1;31mVocê está com obesidade mórbida.')