import random as rd


def sortear_numeros() -> list:
    sorteados = []
    for i in range(6):
        numero = rd.randint(1, 60)
        while(numero in sorteados):
            numero = rd.randint(1, 60)
        sorteados.append(str(numero))
    return sorteados

def main():
    print(print("-----  Questāo 1  -----"))
    print("MEGA SENA - Insira os 6 números da sua aposta 1-60 (s para sair)")
    comando = ''
    qtd = 1
    aposta = []
    while(comando != 's' and qtd < 7):
        comando = input(f"#{qtd}: ")
        try:
            numero = int(comando)
        except:
            print("Precisa ser um número.")
            continue

        if(numero < 1 or numero > 60):
            print("Os número da aposta precisam estar entre 1 e 60")
            continue

        if(numero in aposta):
            print("Número já presente na aposta")
            continue

        print(f"{numero} adicionado a aposta")
        aposta.append(str(numero))
        qtd += 1

    sorteio = sortear_numeros()
    print(f"Aposta: {','.join(aposta)}")
    print(f"Sorteio: {','.join(sorteio)}")
    acertos = 0
    for num in aposta:
        if num in sorteio:
            acertos += 1
    print(f"Total de acertos: {acertos}")


    


if(__name__ == "__main__"):
    main()