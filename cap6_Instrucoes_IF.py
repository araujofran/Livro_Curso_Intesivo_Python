alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n')
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
print('\n')
print('Colocando os 3 dicionarios dentro de uma lista\n')
print(aliens)
print('Validando as posições dentro de uma lista\n')
for p,v in enumerate(aliens):
    print(f'Na posição {p} há o dicionário {v}\n')
print('\n')