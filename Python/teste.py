mulher_menos20 = 0
total_homens = 0
mais_dezoito = 0

def linha():
    print("-" *25)

print("CADASTRE UMA PESSOA")
linha()
while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    linha()

   
    if idade >= 18:
        mais_dezoito += 1

    if sexo == "M":
        total_homens += 1

    if sexo == "F" and idade < 20:
        mulher_menos20 += 1

    opcao = ' '
    while opcao not in "SN":
        opcao = str(input("Quer continuar: ")).strip().upper()[0]
    if opcao == "N":
        break

linha()
print("====== FIM DO PROGRAMA ======")
print(f"Todal de pessoas com mais de 18 anos: {mais_dezoito}.")
print(f"Ao todo temos {total_homens} homens cadastrados.")
print(f"E temos {mulher_menos20} mulheres com menos de 20 anos.")