soma = 0
cont = 0

num = int(input("Digite um número inteiro: "))

cont += 1
maior = num
menor = num
media = 0

opcao = input("Você quer continuar? (SIM/NÃO): ").upper()

while opcao == "SIM":
    num = int(input("Digite um número inteiro: "))
    soma += num
    cont += 1
    opcao = input("Você quer continuar? (SIM/NÃO): ").upper()

    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = soma / cont
print(f"Você digitou {cont} números")
print(f"A média dos {cont} números é {media}")
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print(f"A soma dos {cont} numeros é {soma}")
