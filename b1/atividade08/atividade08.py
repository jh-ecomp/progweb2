def q1():
    produtos = [
        ("Notebook", 3500.00),
        ("Smartphone", 1800.00),
        ("Teclado Mecânico", 250.00),
        ("Mouse Gamer", 150.00),
        ("Monitor 24'", 900.00),
        ("Fone de Ouvido", 120.00),
        ("Cadeira Ergonômica", 850.00),
        ("Impressora", 600.00),
        ("Webcam Full HD", 200.00),
        ("SSD 1TB", 380.00)
    ]

    with open('produtos.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        arquivo.write('"produto","preco"\n')
        for produto in produtos:
            arquivo.write(f'"{produto[0]}",{produto[1]}\n')

        print("Arquivo criado!")

    soma = 0
    qtd = 0

    with open('produtos.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        linhas = arquivo.readline()

        linhas = arquivo.readlines()
        for produto in linhas:
            qtd += 1
            soma += float(produto.split(',')[1])

    print(f"O preço médio dos produtos é: {soma / qtd:.2f}")


def main():
    q1()


if(__name__ == "__main__"):
    q1()