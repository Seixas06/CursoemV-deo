from random import choice,shuffle
import emoji
a1=str(input('Primeiro aluno:'))
a2=str(input('Segundo aluno:'))
a3=str(input('Terceiro aluno:'))
a4=str(input('Quarto aluno:'))
a5=str(input('Quinto aluno:'))
lista=[a1,a2,a3,a4,a5]
shuffle(lista)
#print('O aluno sorteado foi {}. Parabéns 🥳'.format(choice(lista)))
print('A ordem de apresentação será')
print(lista)
print('📚 Boa apresentação!💡')