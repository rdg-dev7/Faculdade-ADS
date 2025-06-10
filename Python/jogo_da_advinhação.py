from random import randint
from time import sleep

tentativas = 1
computador = randint( 0 , 10)
print("=+=" * 20)
print("Vou pensar em um número entre 0 e 10, tente adivinhar... ")
sleep(1)
print("=+=" * 20)
jogador = int(input("Em que número eu pensei? "))
sleep(1)
print("=+=" * 20)
while jogador != computador:
    print("Você errou!")
    sleep(1)
    print("=+=" * 20)
    print("Tente novamente!")
    sleep(2)
    print("=+=" * 20)
    jogador = int(input("Em que número eu pensei? "))
    sleep(1)
    tentativas += 1
print("=+=" * 20)

print("Parabéns! Você acertou o número {} em {} tentativas!".format(computador, tentativas))
print("=+=" * 20)