import json

def q1():
    print("-----  Questāo 1  -----")
    entrada = '''[
    { "nome": "Ana", "idade": 20, "curso": "ADS", "notas": [8.0, 7.5, 9.0] },
    { "nome": "Bruno", "idade": 22, "curso": "Ciência da Computação", "notas": [6.5, 4.0, 7.0] },
    { "nome": "Carolina", "idade": 25, "curso": "Engenharia de Software", "notas": [9.0, 9.5, 10.0] },
    { "nome": "Diana", "idade": 21, "curso": "ADS", "notas": [7.0, 6.0, 8.5] },
    { "nome": "Eduardo", "idade": 23, "curso": "Sistemas de Informação", "notas": [5.5, 5.0, 6.0] }
    ]'''

    entrada_parseada = json.loads(entrada)

    for aluno in entrada_parseada:
        aluno['media'] = (aluno['notas'][0] + aluno['notas'][1] + aluno['notas'][2]) / 3
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

    print()
    print("Aprovados:")
    for aluno in entrada_parseada:
        if(aluno['media'] >= 7):
            print(aluno['nome'])

    print()
    max = ['nome', 0]
    for aluno in entrada_parseada:
        if(aluno['media'] > max[1]):
            max[0] = aluno['nome']
            max[1] = aluno['media']

    print(f"Maior média: {max[0]} - {max[1]:.2f}")    
    
    print()

def q2():
    print("-----  Questāo 2  -----")

    entrada = '''{
    "loja": "TechStore",
    "produtos": [
        { "id": 1, "nome": "Teclado Mecânico", "categoria": "Periféricos", "preco": 250.00, "estoque": 15 },
        { "id": 2, "nome": "Mouse Gamer", "categoria": "Periféricos", "preco": 120.00, "estoque": 5 },
        { "id": 3, "nome": "Monitor 24' 144Hz", "categoria": "Monitores", "preco": 899.90, "estoque": 8 },
        { "id": 4, "nome": "Headset Bluetooth", "categoria": "Áudio", "preco": 199.00, "estoque": 12 },
        { "id": 5, "nome": "Processador Intel i5", "categoria": "Hardware", "preco": 1150.00, "estoque": 6 },
        { "id": 6, "nome": "Placa de Vídeo RTX 4060", "categoria": "Hardware", "preco": 2100.00, "estoque": 4 },
        { "id": 7, "nome": "Memória RAM 16GB DDR4", "categoria": "Hardware", "preco": 320.00, "estoque": 25 },
        { "id": 8, "nome": "SSD NVMe 1TB", "categoria": "Hardware", "preco": 450.00, "estoque": 18 },
        { "id": 9, "nome": "Roteador Wi-Fi 6", "categoria": "Redes", "preco": 280.00, "estoque": 1 },
        { "id": 10, "nome": "Cabo HDMI 2m", "categoria": "Acessórios", "preco": 35.00, "estoque": 50 },
        { "id": 11, "nome": "Microfone Condensador", "categoria": "Áudio", "preco": 340.00, "estoque": 7 },
        { "id": 12, "nome": "Webcam Full HD", "categoria": "Periféricos", "preco": 180.00, "estoque": 14 },
        { "id": 13, "nome": "Gabinete Gamer ATX", "categoria": "Hardware", "preco": 299.00, "estoque": 9 },
        { "id": 14, "nome": "Fonte 650W 80 Plus", "categoria": "Hardware", "preco": 380.00, "estoque": 0 },
        { "id": 15, "nome": "Filtro de Linha 5 Tomadas", "categoria": "Acessórios", "preco": 45.00, "estoque": 30 }
    ]
    }'''

    estoque = json.loads(entrada)
    produtos = estoque['produtos']

    print("==========================================")
    for produto in produtos:
        print(f"ID: {produto['id']}\nNome: {produto['nome']}\nCategoria: {produto['categoria']}\n" \
            f"Preço: {produto['preco']:.2f}\nEstoque: {produto['estoque']}")
        print()

    print("==========================================")
    print("Produtos com baixo estoque (menor que 6):")
    for produto in produtos:
        if(produto['estoque'] < 6):
            print(f"ID: {produto['id']}\nNome: {produto['nome']}\nCategoria: {produto['categoria']}\n" \
                f"Preço: {produto['preco']:.2f}\nEstoque: {produto['estoque']}")
            print()

    print("==========================================")
    for produto in produtos:
        produto['valor_armazenado'] = produto['preco'] * produto['estoque']
        print(f"ID: {produto['id']}\nNome: {produto['nome']}\n" \
            f"Valor total armazenado: R${produto['valor_armazenado']:.2f}")
        print()

    print("==========================================")
    valor_total = 0
    for produto in produtos:
        valor_total += produto['valor_armazenado']

    print(f"O valor total armazenado no estoque é: R${valor_total:.2f}")
    print()

    print("==========================================")
    max_valor = produtos[0]
    for produto in produtos:
        if(produto['valor_armazenado'] > max_valor['valor_armazenado']):
            max = produto

    print(f"Produto de maior valor armazenado:\nID: {max_valor['id']}\nNome: {max_valor['nome']}\nCategoria: {max_valor['categoria']}\n" \
        f"Preço: {max_valor['preco']:.2f}\nEstoque: {max_valor['estoque']}")

    print()

    print("==========================================")

    categorias = [produto['categoria'] for produto in produtos]
    
    pesquisa = input(f"Pesquise os produtos de uma categoria\n({', '.join(categorias)}): ")

    if(pesquisa in categorias):
        for produto in produtos:
            if(produto['categoria'] == pesquisa):
                print(f"ID: {produto['id']}\nNome: {produto['nome']}\nCategoria: {produto['categoria']}\n" \
                    f"Preço: {produto['preco']:.2f}\nEstoque: {produto['estoque']}")
                print()
    else:
        print("Categoria não encontrada.")

    print()



def main():
    q1()
    q2()

if(__name__ == '__main__'):
    q2()