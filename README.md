Conta
    ContaCorrente
    ContaPoupanca
Pessoa
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança) - OK
    Pessoa tem nome e idade (com getters) - OK
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca) - OK
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta - OK
    ContaCorrente deve ter um limite extra - OK
    Contas têm agência, número da conta e saldo - OK
    Contas devem ter método para depósito - OK
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar) - OK

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
