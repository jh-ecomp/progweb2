def q1():
    print("-----  Questāo 1  -----")
    print("Imprimindo os 10 primeiros números da sequência de Fibonacci!")
    n1 = 0
    n2 = 1
    print(f"1º: {n2 + n1}")
    for i in range(2, 11, 1):
        print(f"{i}º: {n2 + n1}")
        n1, n2 = n2, n1 + n2

def q2():
    print("-----  Questāo 2  -----")
    print("Os 10 primeiros números primos são: ", end='')

    num = 1

    for primos in range(1, 10, 1):
        while(num):
            if(num <= 1):
                num +=1
                continue

            if(num == 2):
                print(f"{num} ", end='')
                primos +=1
                num +=1
                continue

            if(num % 2 == 0):
                num +=1
                continue

            div = 3
            while(div < num / 2):
                if(num % div == 0):
                    break
                div += 2
            else:
                print(f"{num} ", end='')
                num +=1
                break

            num +=1
    print()

def q3():
    print("-----  Questāo 3  -----")
    valor = float(input("Digite um número para calcular a raiz quadrada: "))

    if(valor < 0):
        print("Não existe raiz quadrada em R de números negativos!")
        return

    aprox = valor / 2 if valor != 0 else 0

    while True:
        nova_aprox = (aprox + valor / aprox) / 2
        if abs(nova_aprox - aprox) < 0.0001:
            break
        aprox = nova_aprox

    print(f"A raiz quadrada de {valor} é aproximadamente {round(nova_aprox, 4)}")
    print()


def q4():
    print("-----  Questāo 4  -----")
    print("Imprimindo a tabuada de multiplicação de 1 a 10!")
    for i in range(1, 11, 1):
        print(f"Tabuada do {i}:")
        for j in range(1, 11, 1):
            print(f"{i} * {j} = {i * j}")

        print()
    print()

def main():
    q1()
    q2()
    q3()
    q4()

if(__name__ == "__main__"):
    main()