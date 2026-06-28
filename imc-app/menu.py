from models.pessoa import Pessoa
from models.atleta import Atleta
from models.historico import Historico
from exceptions.entrada_invalida import EntradaInvalida

historico = Historico()


def ler_float(msg):
    try:
        valor = float(input(msg))

        if valor <= 0:
            raise EntradaInvalida("O valor deve ser positivo.")

        return valor

    except ValueError:
        raise EntradaInvalida("Digite um número válido.")


def cadastrar_pessoa():
    nome = input("Nome: ")
    idade = int(ler_float("Idade: "))
    peso = ler_float("Peso (kg): ")
    altura = ler_float("Altura (m): ")

    pessoa = Pessoa(nome, idade, peso, altura)

    historico.adicionar(pessoa)

    print("\nPessoa cadastrada com sucesso!\n")


def cadastrar_atleta():
    nome = input("Nome: ")
    idade = int(ler_float("Idade: "))
    peso = ler_float("Peso (kg): ")
    altura = ler_float("Altura (m): ")

    atleta = Atleta(nome, idade, peso, altura)

    historico.adicionar(atleta)

    print("\nAtleta cadastrado com sucesso!\n")


def mostrar_ultimo():
    if not historico.registros:
        print("Nenhuma pessoa cadastrada.")
        return

    pessoa = historico.registros[-1]

    print(f"\nNome: {pessoa.nome}")
    print(f"IMC: {pessoa.calcular_imc():.2f}")
    print(f"Classificação: {pessoa.classificar_imc()}\n")


def executar():

    while True:

        print("===== MENU =====")
        print("1 - Cadastrar pessoa")
        print("2 - Mostrar IMC da última pessoa")
        print("3 - Cadastrar atleta")
        print("4 - Histórico")
        print("0 - Sair")

        try:

            opcao = input("Escolha: ")

            match opcao:

                case "1":
                    cadastrar_pessoa()

                case "2":
                    mostrar_ultimo()

                case "3":
                    cadastrar_atleta()

                case "4":
                    historico.mostrar()

                case "0":
                    print("Encerrando...")
                    break

                case _:
                    raise EntradaInvalida("Opção inválida.")

        except EntradaInvalida as erro:
            print(f"\nErro: {erro}\n")