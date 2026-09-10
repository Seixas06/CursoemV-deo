times= ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'São Paulo', 'Mirassol', 'Fluminense', 'Bragantino', 'Ceará SC',
        'Atlético-MG', 'Internacional', 'Grêmio', 'Corinthias', 'Santos', 'Vasco da Gama', 'EC Vitória', 'Juventude', 'Fortaleza',
        'Sport Recife')
print('-='*30)
print('Tabela do Brasileirão 18/08/2025:')
for t in times:
    print(t)
print('-='*30)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-='*30)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Palmeiras está na {times.index("Palmeiras")+1}ª posição')