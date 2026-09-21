import json
import urllib.request


def obter_cotacao(moeda_origem: str, moeda_destino: str) -> dict:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_origem}-{moeda_destino}"
    try:
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode('utf-8'))
            chave = f"{moeda_origem}{moeda_destino}"
            return dados[chave]
    except Exception as erro:
        print(f"Erro ao obter cotação: {erro}")
        return None


def main():
    opcoes = {
        '1': ('BRL', 'USD'),
        '2': ('EUR', 'USD'),
        '3': ('BTC', 'USD'),
        '4': ('BTC', 'BRL')
    }

    while True:
        print("==== COTAÇÃO ====")
        print("1 - BRL / USD")
        print("2 - EUR / USD")
        print("3 - BTC / USD")
        print("4 - BTC / BRL")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            break

        if opcao in opcoes:
            moeda_origem, moeda_destino = opcoes[opcao]
            cotacao = obter_cotacao(moeda_origem, moeda_destino)
            
            if cotacao:
                valor = float(cotacao['bid'])
                valor_formatado = f"{valor:.4f}" if valor < 10 else f"{valor:.2f}"
                print(f"Conversão: 1 {moeda_origem} = {valor_formatado} {moeda_destino}")
        else:
            print("Opção inválida!")

        print()


if(__name__ == '__main__'):
    main()
