class Futuro:
    """
    Representa um contrato futuro com ajuste diário, margem de manutenção e chamada de margem.
    """

    # TODO: docstring
    def __init__(
        self,
        strike_price: int,
        spot_price: int,
        conta_margem: int,
        margem_inicial: int,
        margem_manutencao: int,
        is_long_position: bool = True,
        tamanho_contrato: int = 100,
    ):
        self.strike_price = strike_price  # TODO: validação de strike e spot
        self.spot_price = spot_price
        self.is_long_position = is_long_position
        self.margem_manutencao = margem_manutencao
        self.margem_inicial = margem_inicial
        self.tamanho_contrato = tamanho_contrato
        self.conta_margem = conta_margem
        self.deposito = 0
        self.saque = 0

    def _verifica_margem(self):
        if self.conta_margem < self.margem_manutencao:
            self.deposito = self.margem_inicial - self.conta_margem
            self.saque = 0
            print(f"Aviso: necessario depositar ${self.deposito}")
        elif self.conta_margem > self.margem_inicial:
            self.saque = self.conta_margem - self.margem_inicial
            self.deposito = 0
            print(f"Aviso: Conta Margem com excedente de ${self.saque}")
        else:
            self.saque = 0
            self.deposito = 0

    def ajuste_diario(self, novo_spot: int):
        self.spot_price = novo_spot
        ajuste_diario = self.tamanho_contrato * (self.spot_price - self.strike_price)
        if not self.is_long_position:
            ajuste_diario *= -1
        self.conta_margem += ajuste_diario
        self._verifica_margem()

    def chamada_margem(self, deposito):
        if deposito < self.deposito:
            print(f"Deposito minimo {self.deposito}")
        else:
            self.conta_margem += deposito
            self._verifica_margem()

    def saque_excedente_margem(self, saque):
        if saque > self.saque:
            print(f"O saque nao pode exceder ${self.saque}")
        else:
            self.conta_margem -= saque
            self._verifica_margem()


if __name__ == "__main__":
    contrato = Futuro(
        strike_price=100,
        spot_price=100,
        conta_margem=1000,
        margem_inicial=1000,
        margem_manutencao=800,
        is_long_position=True,
        tamanho_contrato=10,
    )
    contrato.ajuste_diario(105)
    contrato.saque_excedente_margem(contrato.saque + 10)
    contrato.saque_excedente_margem(contrato.saque)
    print(contrato.conta_margem)
    contrato.ajuste_diario(75)
    contrato.chamada_margem(contrato.deposito - 10)
    contrato.chamada_margem(contrato.deposito)
    print(contrato.conta_margem)
