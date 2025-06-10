valor =  0
def mostra_linha():
    print('-' * 20)
while True:
    mostra_linha()
    valor = int(input('Quer ver a tabuada de  qual valor? '))
    mostra_linha()
    if valor < 0:
        break
    for n in range (1, 11):
        mostra_linha()
        print(f'{valor} x {n} = {valor * n}')
print('Programa tabuada encerrado!')
