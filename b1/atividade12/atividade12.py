class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome}!")


class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"{self.marca} {self.modelo} está ligado.")


class Eletrico(Carro):
    def ligar(self):
        print(f"{self.marca} {self.modelo} elétrico está ligado.")


def apresentar_familia(familia: list[Pessoa]):
    for pessoa in familia:
        pessoa.falar()


def q1():
    print("-----  Questão 1  -----")
    p = Pessoa("Carlos", 25)
    p.falar()
    print()


def q2():
    print("-----  Questão 2  -----")
    carro = Carro("Toyota", "Corolla")
    carro.ligar()
    eletrico = Eletrico("BYD", "Dolphin")
    eletrico.ligar()
    print()


def q3():
    print("-----  Questão 3  -----")
    familia = [
        Pessoa("Carlos", 45),
        Pessoa("Ana", 42),
        Pessoa("Lucas", 16)
    ]
    apresentar_familia(familia)
    print()


def main():
    q1()
    q2()
    q3()


if(__name__ == '__main__'):
    main()

