class Historico:

    def __inicio__(self):
        self.registros = []

    def adicionar(self, pessoa):
        self.registros.append(pessoa)

    def mostrar(self):
        if not self.registros:
            print("\nNenhum cálculo realizado.\n")
            return

        print("\n===== HISTÓRICO =====")

        for pessoa in self.registros:
            print(
                f"{pessoa.nome} | "
                f"IMC:{pessoa.calcular_imc():.2f} | "
                f"{pessoa.classificar_imc()}"
            )
        print()

    