
saldo = 0
limite = 500
limite_saques = 3
saque_diario = 0


def print_hi(name):
    print("\n\n")
    print(f'Bem vindo ao {name}')
    print(f'''
        =========MENU=========
        q = Sair
        d = Depositar
        s = Sacar
        e = Extrato
        ======================
    ''')


def depositar():
    global saldo
    valor = None

    print(f'Seu saldo é de R${saldo:.2f}')
    valor = input('Quanto quer depositar?\n')
    fvalor = float(valor)
    saldo += fvalor

    print(f'Novo saldo é de R${saldo:.2f}')
    pause()


def sacar():
    global saldo, saque_diario, limite, limite_saques

    print(f'Seu saldo é de R${saldo:.2f}')
    valor = input('Quanto deseja sacar?\n')
    fvalor = float(valor)
    if fvalor > limite:
        print('Saque maior que R$500,00 não permitido')
    else:
        if saque_diario >= limite_saques:
            print('Limite de saques diário de 3 saques, foi atingido!')
        else:
            if fvalor > saldo:
                print('Este valor não está disponível em conta')
            else:
                saldo -= fvalor
                saque_diario += 1
                print(f'Novo saldo é de R${saldo:.2f}')
                print(f'Quantidade de saques remanecentes para hoje:{limite_saques - saque_diario}')

    pause()

def extrato(saldo):
    print(f'Seu saldo é de R${saldo:.2f}')
    pause()


def sair():
    print('Sistema finalizado..')


def pause():
    input('Aperte qualquer tecla para voltar ao menu..')


if __name__ == '__main__':
    print_hi('Sistema Bancário')

    while True:
        opcao = input('Escolha apção de acordo com o menu\n')
        if opcao == 'q':
            sair()
            break
        elif opcao == 'd':
            depositar()
        elif opcao == 's':
            sacar()
        elif opcao == 'e':
            extrato(saldo)
        else:
            print('Opção não valida para o menu')

        print_hi('Sistema Bancário')

