brasileirao = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras',
               'Flamengo', 'Fortaleza', 'Fluminense', 'Athletico-PR',
               'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional',
               'Corinthians', 'Santos', 'Cruzeiro', 'Bahia',
               'Vasco da Gama', 'Goiás', 'Coritiba', 'América-MG')
print('-='*15)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-='*15)
print(f'Os 5 primeiros são: {brasileirao[:6]}')
print('-='*15)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*15)
print(f'O Internacional está na {(brasileirao.index("Internacional")+1)}ª posição.')
print('-='*15)