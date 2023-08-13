#Kaik Mendes
#Github.com/snootic

#Sistema bancário simples v1

print('Bem vindo ao nosso sistema bancário!')
print('Digite a operação desejada como indicado abaixo:')
menu=('''==============================
[1] Visualizar Saldo
[2] Depositar
[3] Sacar
[4] Extrato
[0] Sair
==============================''')

saldo = float(0)
limite_valor_saque = float(500)
quantidade_saques_diarios = int(3)
extrato = ''

while True:
    print(menu)
    escolha = int(input("digite a operação desejada: "))

    if escolha == 1:
        print(f"\nSeu saldo atual é de: R$ {saldo:.2f}")

    elif escolha == 2:
        valor_deposito = input("Digite o valor a ser depositado: ").replace(',','.')
        if float(valor_deposito) < 0:
            print('\nImpossível depositar um valor inexistente.')
        else:
            saldo += float(valor_deposito)
            extrato += f'\ndéposito: R$ {float(valor_deposito):.2f}'

    elif escolha == 3:
        valor_saque = input("Digite o valor do saque: ").replace(',','.')

        if saldo - float(valor_saque) < 0:
            print('\nSem saldo suficiente para sacar.')
        elif float(valor_saque) > limite_valor_saque:
            print('\nImpossível sacar mais do que R$ 500.00.')
        elif quantidade_saques_diarios == 0:
            print('\nLimite de saque diário atingido, volte amanhã.')
        else:
            saldo -= float(valor_saque)
            quantidade_saques_diarios -= 1
            extrato += f'\nsaque: R$ {float(valor_saque):.2f}'

    elif escolha == 4:
        print('Extrato'.center(20,"="))
        print(extrato)
        print(f'\nSaldo: {saldo}\n'+"="*20)

    elif escolha == 0:
        break

    else:
        print('\nOpção inválida. Por favor, escolha uma das opções indicadas.')
