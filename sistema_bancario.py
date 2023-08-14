#Kaik Mendes
#Github.com/snootic

#Sistema bancário simples v2

print('Bem vindo ao nosso sistema bancário!')
print('Digite a operação desejada como indicado abaixo:')
menu_login = ('''==============================
[1] Logar
[2] Criar uma conta
[3] Criar usuário
[4] Visualizar contas
[5] Visualizar usuários
[0] Sair
==============================''')
              
menu=('''==============================
[1] Visualizar Saldo
[2] Depositar
[3] Sacar
[4] Extrato
[0] Sair
==============================''')

saldo = float(0)
saques_utilizados = int(0)
extrato = []
AGENCIA = "0001"
usuarios_cadastrados = {}
contas = 0
contas_cadastradas = {}


def criar_usuario():
    cpf = int(input('Digite o CPF (apenas dígitos): '))
    if usuarios_cadastrados.get(f'{cpf}') != None:
        print('CPF já cadastrado')
    else:
        nome = str(input('Digite o nome: '))
        data_de_nascimento = str(input('Digite a data de nascimento: '))
        endereço = str(input('Digite seu endereço completo (Rua, N° - Bairro - Cidade/UF): '))
        cliente = {"nome": nome, "data de nascimento": data_de_nascimento, "endereço": endereço}
        usuarios_cadastrados[f'{cpf}'] = cliente
        print('Usuário criado com sucesso')

def criar_conta():
    cpf = int(input('Digite o CPF da conta(apenas dígitos): '))
    if usuarios_cadastrados.get(f'{cpf}') == None:
        print('CPF não cadastrado')
    else:
        conta = contas + 1
        contas_cadastradas[f"{conta}"] = {"agencia": AGENCIA, "usuario": f'{cpf}'}
        print('Conta criada com sucesso')

def visualizar_contas():
    print(contas_cadastradas)

def visualizar_usuarios():
    print(usuarios_cadastrados)

def logar():
    while True:
        print(menu_login)
        escolha = int(input('Digite a opção desejada: '))
        if escolha == 1:
            agencia = input('Digite o número da agência: ')
            conta = input('Digite o número da conta: ')
            cpf = input('Digite o CPF cadastrado: ')
            if contas_cadastradas.get(f'{conta}') != None and agencia == AGENCIA and cpf == contas_cadastradas[f'{conta}']['usuario']:
                return True
            else:
                print('Conta inválida')

        elif escolha == 2:
            criar_conta()

        elif escolha == 3:

            criar_usuario()
        
        elif escolha == 4:
            visualizar_contas()
        
        elif escolha == 5:
            visualizar_usuarios()

        elif escolha == 0:
            print("Obrigado por escolher nossos serviços!")
            break
        else:
            print('escolha uma opção válida')


def depositar_dinheiro(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor}')
    else:
        print('Impossível depositar valor inexistente.')
    return saldo, extrato

def sacar_dinheiro(*, saldo, valor, extrato, saques):
    LIMITE_VALOR_SAQUE = float(500)
    LIMITE_SAQUE_DIARIOS = int(3)
    if saldo - valor < 0:
        print('Saldo insuficiente')
    elif saques == LIMITE_SAQUE_DIARIOS:
        print('Limite de saques diários atingido, volte amanhã.')
    elif valor > LIMITE_VALOR_SAQUE:
        print('Não é possível sacar mais do que R$ 500.00')
    elif valor <=0:
        print('Não é possível sacar esse valor.')
    else:
        saldo -= valor
        saques += 1
        extrato.append(f'Saque: R$ {valor}')
    return saldo, extrato, saques

def visualizar_extrato(saldo, /, *, extrato):
    extrato_final = extrato.copy()
    extrato_final.append(f'Saldo: {saldo}')
    print('Extrato'.center(20, "="))
    for item in extrato_final:
        print(item)
    print('='*20)

if logar():
    while True:
        print(menu)
        escolha = int(input("digite a operação desejada: "))

        if escolha == 1:
            print(f"\nSeu saldo atual é de: R$ {saldo:.2f}")

        elif escolha == 2:
            valor = input("Digite o valor para depósito: ").replace(',','.')
            valor = float(valor)

            saldo, extrato = depositar_dinheiro(saldo, valor, extrato)
            
        elif escolha == 3:
            valor = input("Digite o valor para o saque: ").replace(',','.')
            valor = float(valor)
            
            saldo, extrato, saques_utilizados = sacar_dinheiro(saldo=saldo, valor=valor,
            extrato=extrato, saques=saques_utilizados)

        elif escolha == 4:
            visualizar_extrato(saldo, extrato=extrato)

        elif escolha == 0:
            logar()

        else:
            print('\nOpção inválida. Por favor, escolha uma das opções indicadas.')

