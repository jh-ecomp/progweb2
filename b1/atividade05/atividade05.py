import random

def q1():
    print("-----  Questāo 1  -----")
    print("Gerando uma lista de 20 elementos com valores aleatórios de 0 a 10!")
    numeros = [random.randint(0, 10) for i in range(20)]
    repetidos = []
    numeros.sort()
    print(numeros)
    inicio = 0
    fim = 0
    print((fim < len(numeros)) and (numeros[fim] == numeros[inicio]))

    while(fim < len(numeros)):

        while((fim < len(numeros)) and (numeros[fim] == numeros[inicio])):
            fim += 1
        
        
        if(fim - inicio > 1):
            repetidos.append(numeros[inicio])

        inicio = fim

    print(f"Os números repetidos são: {repetidos}")
    print()

def q2():
    print("-----  Questāo 2  -----")
    print("Coletando texto para análise:")
    texto = ''
    palavras = []

    while True:
        texto = input("Digite uma palavra (s para sair): ")

        if(texto == 's'): break

        palavras.append(texto)

    filtradas = [p for p in palavras if(p == p.upper() and len(p) > 4)]
    print(f"A lista de palavras criada foi {palavras}")
    print(f"A lista de palavras com todas as letras em maiúsculo e comprimento maior que 4 é {filtradas}")
    
    print()

def q3():
    print("-----  Questāo 3  -----")
    print("Coletando pares de números para análise:")
    texto = ''
    numeros = []

    while True:
        texto = input("Digite o primeiro número (s para sair): ")
        if(texto == 's'): break
        primeiro = int(texto)
        texto = input("Digite o segundo número (s para sair): ")
        if(texto == 's'): break
        segundo = int(texto)

        numeros.append((primeiro, segundo))

    tupla = tuple(numeros)
    print(f"Entrada: {tupla}")
    segundos = ' + '.join(str(x[1]) for x in tupla)
    soma = 0
    for par in tupla:
        soma += par[1]

    print(f"Soma dos segundos elementos: {soma} ({segundos})")

    print()

def q4():
    print("-----  Questāo 4  -----")
    print("Coletando pares de números para análise:")
    texto = ''
    numeros = []

    while True:
        texto = input("Digite o primeiro número (s para sair): ")
        if(texto == 's'): break
        primeiro = int(texto)
        texto = input("Digite o segundo número (s para sair): ")
        if(texto == 's'): break
        segundo = int(texto)

        numeros.append((primeiro, segundo))

    numeros = [list(par) for par in numeros]
    print(f"Entrada: {numeros}")

    modificados = [[par[0], par[1] + 10] for par in numeros]
    print(f"Saída: {modificados}")

    print()

def q5():
    print("-----  Questāo 5  -----")
    numero = int(input("Digite um número: "))

    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            print(f"{j}", end='')
        print("\n", end='')

    for i in range(numero - 1, 0, -1):
        for j in range(1, i + 1):
            print(f"{j}", end='')
        print("\n", end='')


def main():
    q1()
    q2()
    q3()
    q4()
    q5()

if(__name__ == '__main__'):
    main()