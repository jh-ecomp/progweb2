
def q1():
    print("-----  Questāo 1  -----")
    valor1 = int(input("\tDigite o primeiro número: "))
    valor2 = int(input("\tDigite o segundo número: "))
    valor3 = float(input("\tDigite o terceiro número: "))
    print("\tO produto do dobro do primeiro com a metade do segundo é: ", (2 * valor1) * (valor2 / 2))
    print("\tA soma do triplo do primeiro com o terceiro é: ", (valor1 * 3) + valor3)
    print("\tO cubo do terceiro é: ", valor3 * valor3 * valor3)

if(__name__ == '__main__'):
    q1()