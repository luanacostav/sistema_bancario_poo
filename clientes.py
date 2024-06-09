from dataclasses import dataclass, field
# ============================== ABSTRATA ==============================


@dataclass
class Pessoa:
    _nome: str
    _idade: int

    @property
    def nome_pessoa(self):
        return self._nome

    @nome_pessoa.setter
    def nome_pessoa(self, nome: str):
        if len(nome) > 0:
            self._nome = nome
        else:
            raise Exception("Nome inválido")

    @property
    def idade_pessoa(self):
        return self._idade

    @idade_pessoa.setter
    def idade_pessoa(self, idade: int):
        self._idade = idade

# ============================== SUBCLASSE ==============================


@dataclass
class Cliente(Pessoa):
    contas: list = field(default_factory=list)

    def cliente_contas(self, *conta) -> list:
        self.contas.extend(conta)
        return self.contas

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self._nome!r}, {self._idade!r})'
        return f'{class_name} {attrs}'

# ============================== INSTÂNCIA ==============================


if __name__ == '__main__':
    import contas

    c1 = Cliente("Luana", 21)
    conta_p = contas.ContaPoupanca(1, 123, 100)
    conta_c = contas.ContaCorrente(1, 321, 200, 100)

    c1.cliente_contas(conta_p, conta_c)

    print(c1)
