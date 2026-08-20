
def q1():
    print("-----  Questāo 1  -----")
    valor1 = int(input("\tDigite o primeiro número: "))
    valor2 = int(input("\tDigite o segundo número: "))
    valor3 = float(input("\tDigite o terceiro número: "))
    print("\tO produto do dobro do primeiro com a metade do segundo é: ", (2 * valor1) * (valor2 / 2))
    print("\tA soma do triplo do primeiro com o terceiro é: ", (valor1 * 3) + valor3)
    print("\tO cubo do terceiro é: ", valor3 * valor3 * valor3)
    print("\n")

def q2():
    print("-----  Questāo 2  -----")
    while(1):
        valor1 = int(input("\tDigite um número inteiro e positivo para \n" \
        "\tverificar se é primo (0 para sair): "))

        if(valor1 == 0):
            break

        if(valor1 <= 1):
            print(f"\t{valor1} nāo é primo!")
            continue

        if(valor1 % 2 == 0):
            print(f"\t{valor1} nāo é primo!")
            continue

        div = 3
        while(div < valor1 / 2):
            if(valor1 % div == 0):
                print(f"\t{valor1} nāo é primo!")
                break
            div += 2
        else:
            print(f"\t{valor1} é primo!")

        print("\n")
    print("\n")

def q3():
    print("-----  Questāo 3  -----")
    valor1 = int(input("\tDigite o número para a soma do quadrado dos dígitos: "))
    soma = 0
    resto = valor1
    while(resto > 0):
        soma += int((resto % 10) * (resto % 10))
        resto = resto / 10
    print(f"\t O resultado da soma dos quadrados dos dígitos de {valor1} é: {soma}")
    print("\n")

def q4():
    print("-----  Questāo 4  -----")
    valor1 = int(input("\tDigite o número inteiro positivo para verificar se é perfeito: "))
    soma = 0
    if(valor1 < 0):
        print(f"\t{valor1} nāo é")
    if(valor1 == 0):
        print("\t0 nāo é um número perfeito! 0 nāo tem divisores!")
        return

    if(valor1 == 1):
        print("\t1 é um número perfeito!\n" \
              "A soma de seus divisores é 1")
    
    for div in range(1, int(valor1 / 2) + 1):
        if(valor1 % div == 0):
            soma += div

    if(soma == valor1):
        print(f"\t{valor1} é um número perfeito!\n" \
              f"\tA soma de seus divisores é {soma}")
    else:
        print(f"\t{valor1} nāo é um número perfeito!\n" \
              f"\tA soma de seus divisores é {soma}")

    print("\n")

def main():
    q1()
    q2()
    q3()
    q4()

if(__name__ == '__main__'):
    main()