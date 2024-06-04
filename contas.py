from abc import ABC, abstractmethod

# ============================== ABSTRATA ==============================


class Conta(ABC):
    def __init__(
        self, agencia: int, numero: int, _saldo: float = 0
    ) -> None:
        self.agencia = agencia
        self.numero = numero
        self._saldo = _saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self._saldo += valor
        self.info(f'(Depósito R$ {valor})')
        return self._saldo

    def info(self, msg: str = '') -> None:
        print(f'SALDO: {self._saldo:.2f} {msg}')
        print("---")

# ============================== SUBCLASSES ==============================


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor

        if valor_pos_saque >= 0:
            self._saldo -= valor
            self.info(f'(Saque R$ {valor})')
        else:
            raise Exception("Não foi possível sacar")

        return self._saldo

    def depositar(self, valor):
        return super().depositar(valor)


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, numero: int, _saldo: float = 0,
        limite: float = 0
    ):
        super().__init__(agencia, numero, _saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor
        limite_max = - self.limite

        if valor_pos_saque >= limite_max:
            self._saldo -= valor
            self.info(f'(Saque R$ {valor}) | (Limite R$ {self.limite})')
        else:
            self.info(f'[Saque Negado! -> {valor}]')
            raise Exception("Não foi possível sacar")

        return self._saldo

    def depositar(self, valor):
        return super().depositar(valor)

# ============================== INSTÂNCIA ==============================


if __name__ == '__main__':
    conta_p = ContaPoupanca(123, 1, 100)
    conta_p.depositar(200)
    conta_p.sacar(100)
    # conta_p.sacar(500) -> raise EXCEPTION

    print()

    conta_c = ContaCorrente(123, 2, 100, 100)
    conta_c.depositar(200)
    conta_c.sacar(150)
