import json
import re
from datetime import datetime as dt

def q1():
    print("-----  Questāo 1  -----")
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
    print()

def insere_estoque(id: str, nome: str, qtd: int, valor_uni: float) -> bool:
    try:
        with open('q2.json', mode='r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            estoque = json.loads(conteudo) if conteudo else {}
    except (FileNotFoundError, json.JSONDecodeError):
        estoque = {}

    produto = {"id": id, "nome": nome, "qtd": qtd, "valor_uni": valor_uni}
    estoque[str(id)] = produto

    try:
        with open('q2.json', mode='w', encoding='utf-8') as arquivo:
            json.dump(estoque, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao inserir produto: {e}\n")
        return False


def remove_estoque(id: str) -> bool:
    try:
        with open('q2.json', mode='r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            estoque = json.loads(conteudo) if conteudo else {}
    except (FileNotFoundError, json.JSONDecodeError):
        estoque = {}
        print("Arquivo vazio!\n")
        return False

    if(estoque[id]):
        estoque.pop(id)
        try:
            with open('q2.json', mode='w', encoding='utf-8') as arquivo:
                json.dump(estoque, arquivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erro ao remover produto: {e}\n")
            return False
    else:
        print("Produto não existe no estoque!\n")
        return False


def lista_estoque():
    try:
        with open('q2.json', mode='r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            estoque = json.loads(conteudo) if conteudo else {}
    except (FileNotFoundError, json.JSONDecodeError):
        estoque = {}
        print("Arquivo vazio!")
        return

    for produto in estoque.values():
        print(f"Id: {produto['id']} | Nome: {produto['nome']} | Quantidade: {produto['qtd']} | Valor unitário: {produto['valor_uni']}")

    print()

def q2():
    print("-----  Questāo 2  -----")
    while(True):
        comando = input("Informe a opção desejada\n" \
                        "1- Cadastro de produtos\n" \
                        "2- Remover produtos\n" \
                        "3- Listar produtos\n" \
                        "0- Sair\n")
        
        match(comando):
            case '1':
                id = input("Id: ")
                nome = input("Nome: ")
                qtd = int(input("Qtd: "))
                valor_uni = float(input("Valor unitário: "))
                if(insere_estoque(id, nome, qtd, valor_uni)):
                    print(f"Produto {id}, inserido com sucesso!\n")
                else:
                    print("Falha ao inserir produto!\n")
            case '2':
                id = input("Insira o Id do produto a ser removido: ")
                if(remove_estoque(id)):
                    print(f"Produto {id}, removido com sucesso!\n")
                else:
                    print("Falha ao remover produto!\n")
            case '3':
                lista_estoque()
            case '0':
                print("Finalizando sistema!")
                break
            case _:
                continue

    print()


def q3():
    print("-----  Questāo 3  -----")
    qtd_palavras = 0
    with open('diario.txt', mode='r') as diario:
        linha = diario.readline()

        while(linha):
            palavras = re.sub('[^a-zA-Z ]+', '*', linha).split(' ')
            qtd_palavras += len(palavras)
            linha = diario.readline()

        print(f"Data: {dt.now().date()} | Quantidade de palavras: {qtd_palavras}")

    with open('diario.txt', mode='a') as diario:
        diario.write(f"\nData: {dt.now().date()} | Quantidade de palavras: {qtd_palavras}")

def q4():
    print("-----  Questāo 3  -----")
    qtd = 0

    try:
        with open('contador.txt', mode='r') as contador:
            qtd = int(contador.readline())
    except FileNotFoundError:
        with open('contador.txt', mode='w') as contador:
            contador.write('0')
        qtd = 0

    qtd += 1
    print(f"Este sistema já foi acessado {qtd} vezes.")

    with open('contador.txt', mode='w') as contador:
        contador.write(str(qtd))



def main():
    q1()
    q2()
    q3()
    q4()


if(__name__ == "__main__"):
    main()