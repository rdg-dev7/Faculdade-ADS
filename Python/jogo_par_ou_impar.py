from random import randint

cont = 0

def linha():
    print('=-' * 15)

linha()
print('VAMOS JOGAR PAR OU ÍMPAR')
linha()
while True:
    jogador = int(input('Diga um valor: '))
    linha()
    computador = randint(0, 10)
   # opcao = str(input('Par ou ímpar? [P/I]: ' )).upper()

    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I}: ')).upper()[0]

    if tipo == 'P' and soma % 2 == 0 :
        cont += 1
        print(f'Você jogou {jogador} e o computador jogou {computador}, Total deu {soma}, deu PAR')
        linha()
        print('Você VENCEU' )
        print('Vamos jogar novamente')
        linha()

    if tipo == 'P' and soma % 2 != 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}, Total deu {soma}, deu ÍMPAR')
        linha()
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes')
        linha()
        break

    if tipo == 'I' and soma % 2 != 0:
        cont += 1
        print(f'Você jogou {jogador} e o computador jogou {computador}, Total deu {soma}, deu ÍMPAR')
        linha()
        print('Você VENCEU!')
        print('Vamos jogar novamente')

    if tipo == 'I' and soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}, Total deu {soma}, deu PAR')
        linha()
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes')
        linha()
        break