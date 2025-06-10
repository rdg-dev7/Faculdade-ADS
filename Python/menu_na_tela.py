valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:

    print('''MENU
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos valores
    [ 5 ] sair do programa''')
    opcao = (int(input("Escolha uma opção: ")))

    if opcao == 1:
        print("O resultado da soma dos dois valores é {}.".format(valor1 + valor2))
    elif opcao == 2:
        print("O resultado da multiplicação dos dois valores é {}.".format(valor1 * valor2))
    elif opcao == 3:
        if valor1 > valor2:
            print("O valor {} é maior.".format(valor1))
        elif valor2 > valor1:
            print("O valor {} é maior.".format(valor2))
        else:
            print("Os dois valores são iguais.")
    elif opcao == 4:
        valor1 = int(input("Digite o primeiro novo valor: "))
        valor2 = int(input("Digite o segundo novo valor: "))
    elif opcao == 5:
        print("Finalizando o programa...")
    else:
        print("Opção inválida! Escolha uma opção no MENU.")