import re

def q1():
    print("-----  Questão 1  -----")
    frase = input("Digite uma frase: ")
    palavras = re.findall(r'\b\w+\b', frase.lower())
    
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1

    print(f"Dicionário de frequências: {frequencia}")
    for palavra, contagem in frequencia.items():
        print(f"'{palavra}': {contagem}")
    print()


def q2():
    print("-----  Questão 2  -----")
    medias = {}
    print("Cadastro de notas dos alunos (digite 's' no nome para finalizar):")
    
    while True:
        nome = input("Digite o nome do aluno: ")
        if(nome == 's'):
            break

        notas_str = input(f"Digite as notas de {nome} separadas por espaço: ")
        try:
            notas = [float(nota) for nota in notas_str.split()]
            if not notas:
                print("Nenhuma nota informada.")
                continue
            media = sum(notas) / len(notas)
            medias[nome] = round(media, 2)
        except ValueError:
            print("Entrada inválida de notas. Tente novamente.")
            continue

    print(f"Dicionário de médias: {medias}")
    for aluno, media in medias.items():
        print(f"Aluno: {aluno} | Média: {media:.2f}")
    print()


def q3():
    print("-----  Questão 3  -----")
    carrinho = {}
    print("Adicionando itens ao carrinho de compras (digite 's' no produto para finalizar):")
    
    while True:
        produto = input("Digite o nome do produto: ")
        if(produto == 's'):
            break

        try:
            quantidade = int(input(f"Digite a quantidade de '{produto}': "))
        except ValueError:
            print("Quantidade precisa ser um número inteiro.")
            continue

        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        print(f"'{produto}' adicionado ao carrinho! (Quantidade total: {carrinho[produto]})\n")

    print(f"Carrinho de compras: {carrinho}")
    for produto, qtd in carrinho.items():
        print(f"Produto: {produto} | Quantidade: {qtd}")
    print()


def q4():
    print("-----  Questão 4  -----")
    convidados = {}
    print("Inserindo convidados da festa (digite 's' para finalizar):")
    
    while True:
        nome = input("Digite o nome do convidado: ")
        if(nome == 's'):
            break
        if not nome.strip():
            continue

        nome = nome.strip().title()
        convidados[nome] = convidados.get(nome, 0) + 1

    print(f"Dicionário de convidados: {convidados}")
    for nome, qtd in convidados.items():
        print(f"Convidado: {nome} | Ocorrências: {qtd}")
    print()


def obter_signo(dia: int, mes: int) -> str:
    signos = {
        1: (19, "Capricórnio", "Aquário"),
        2: (18, "Aquário", "Peixes"),
        3: (20, "Peixes", "Áries"),
        4: (19, "Áries", "Touro"),
        5: (20, "Touro", "Gêmeos"),
        6: (20, "Gêmeos", "Câncer"),
        7: (22, "Câncer", "Leão"),
        8: (22, "Leão", "Virgem"),
        9: (22, "Virgem", "Libra"),
        10: (22, "Libra", "Escorpião"),
        11: (21, "Escorpião", "Sagitário"),
        12: (21, "Sagitário", "Capricórnio")
    }
    limite, signo_antes, signo_depois = signos[mes]
    return signo_antes if dia <= limite else signo_depois


def q5():
    print("-----  Questão 5  -----")
    try:
        dia = int(input("Digite o dia de nascimento: "))
        mes = int(input("Digite o mês de nascimento (1-12): "))
        ano = int(input("Digite o ano de nascimento: "))
    except ValueError:
        print("Valores de data precisam ser números inteiros.")
        print()
        return

    if(mes < 1 or mes > 12 or dia < 1 or dia > 31):
        print("Data inválida!")
        print()
        return

    signo = obter_signo(dia, mes)
    print(f"Data de nascimento: {dia:02d}/{mes:02d}/{ano} - Signo: {signo}")
    print()


def main():
    q1()
    q2()
    q3()
    q4()
    q5()


if(__name__ == '__main__'):
    main()
