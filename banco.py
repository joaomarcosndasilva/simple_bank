from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main()-> None:
    menu()

def menu() -> None:
    print('=========================================================')
    print('=======================ATM===============================')

    print('=====================BRUTUS BANK=========================')
    print('1 - Criar Conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair')
    print('=========================================================')
    opc: int = int(input('Digite a opção desejada: '))


    if opc == 1:
        criar_conta()
    elif opc == 2:
        efetuar_saque()
    elif opc == 3:
        efetuar_deposito()
    elif opc == 4:
        efetuar_transferencia()
    elif opc == 5:
        listar_contas()
    elif opc == 6:
        print('Volte sempre...')
        sleep(2)
        exit(0)
    else:
        print("Você digitou uma opção inválida, por favor tente novamente!")
        sleep(3)
        menu()



def criar_conta() -> None:
    print('Informe os dados do cliente:')
    nome: str = input('Nome do cliente: ')
    email: str = input("E-mail do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Data de nascimento do cliente: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)
    print('Conta criada com sucessos')
    print('Dados da conta: ')
    print('==========================')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = input('Informe o número da sua conta: ')

        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = input('Informe o valor do saque: ')
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta de número {numero}!')

    else:
        print('Ainda não existem contas cadastradas!')
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    pass


def efetuar_transferencia() -> None:
    pass


def listar_contas() -> None:
    pass


def buscar_conta_por_numero(numero: int) -> Conta:
    pass


if __name__ == '__main__':
    menu()

