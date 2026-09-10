from time import sleep
def maior(* núm):
    maior=0
    print('Analisando os valores passados...')
    if len(núm)==0:
        if len(núm)==0:
            print('Não foram informados valores')
    else:
        for n in núm:
            print(f'{n}',end=' ',flush=True)
            if n>maior:
                maior=n
            sleep(0.4)
        print()
        print(f'Foram informados {len(núm)} valores ao todo')
        print(f'O maior valor informado foi {maior}')
    print('=-'*30)
    sleep(2)


print('=-'*30)
maior(1,4,72,68,9,12,5)
maior(5,9,10)
maior(26,17)
maior(6)
maior()
