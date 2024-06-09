import clientes
import contas
from dataclasses import dataclass, field

# ============================== CLASSE ==============================


@dataclass
class Banco:
    agencias: list[int] = field(default_factory=list)
    cliente_banco: list[clientes.Cliente] = field(default_factory=list)
    conta_banco: list[contas.Conta] = field(default_factory=list)

    def checar_agencia(self, conta) -> bool:
        if conta.agencia in self.agencias:
            return True
        print('checar_agencia', False)
        return False

    def checar_cliente(self, cliente) -> bool:
        if cliente in self.cliente_banco:
            return True
        print('checar_cliente', False)
        return False

    def checar_conta(self, conta) -> bool:
        if conta in self.conta_banco:
            return True
        print('checar_conta', False)
        return False

    def checar_conta_cliente(self, conta, cliente) -> bool:
        if conta in cliente.contas:
            return True
        print('checa_conta_cliente', False)
        return False

    def auth(self, cliente: clientes.Cliente, conta: contas.Conta) -> bool:
        return self.checar_agencia(conta) and \
            self.checar_conta(conta) and \
            self.checar_cliente(cliente) and \
            self.checar_conta_cliente(conta, cliente)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        contas_user = [(conta.agencia, conta.numero)
                       for conta in self.conta_banco]
        attrs = f'{self.agencias!r} | {self.cliente_banco!r} | {contas_user}'

        return f'{class_name} {attrs}'

# ============================== INSTÂNCIA ==============================


if __name__ == '__main__':

    # .......... Criando clientes ..........
    c1 = clientes.Cliente("Luana", 21)
    c2 = clientes.Cliente("João", 20)
    c3 = clientes.Cliente("Gabi", 21)

    # .......... Criando contas ..........
    cp1 = contas.ContaPoupanca(000, 123, 100)
    cc1 = contas.ContaCorrente(1, 321, 200, 100)
    cc2 = contas.ContaCorrente(111, 321, 200, 100)

    # ..... Agregando contas ao cliente .....
    contas_1 = c1.cliente_contas(cp1, cc1)
    contas_2 = c2.cliente_contas(cc2)

    # .......... Criando banco ..........
    banco = Banco()

    # ..... Agregando conta e cliente ao banco .....
    banco.cliente_banco.extend([c1, c2])
    banco.conta_banco.extend(contas_1)
    banco.conta_banco.extend(contas_2)
    banco.agencias.extend([111, 000])
    banco.agencias.extend([1, 2, 3])
    banco.agencias.extend([])
    print("\nPRESENTES NO BANCO:")
    print(banco, "\n")

    # .......... Autenticando ..........
    print("AUTENTICANDO...\n")
    banco.auth(c1, cp1)
    print()
    banco.auth(c1, cc1)
    print()
    banco.auth(c3, cp1)
    print()
    banco.auth(c2, cc2)

    # ..... Depois da autenticação .....
    print("\nAUTENTICADO.\n")
    if banco.auth(c1, cp1):
        cp1.depositar(100)
        print(cp1.info)
