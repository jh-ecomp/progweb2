import random

def calcular_media(n1: int, n2: int, n3: int) -> float:
    return (n1 + n2 + n3) / 3

def contar_pares(n: int) -> int:
    return n // 2 + 1

def gera_n() -> int:
    return random.randint(1, 100)

def calculadora(n1: int, n2: int, op: str) -> str:
    match op:
        case '+':
            return str(n1 + n2)
        case '-':
            return str(n1 - n2)
        case '*':
            return str(n1 * n2)
        case '/':
            if(n2 == 0):
                return 'Erro: divisão por 0'
            return f'{n1 / n2:.2f}'
        case _:
            return 'Operação inválida'

def estatisticas(*args) -> str:
    if not args:
        return  "soma: 0,\n" \
                "media: 0,\n" \
                "maior: None,\n" \
                "menor: None" 
    
    soma = sum(args)
    media = soma / len(args)
    maior = max(args)
    menor = min(args)
    
    return f"soma: {soma},\n" \
        f"media: {media},\n" \
        f"maior: {maior},\n" \
        f"menor: {menor}"


def q1():
    print("-----  Questāo 1  -----")
    nota1 = int(input("Digite a 1ª nota: "))
    nota2 = int(input("Digite a 2ª nota: "))
    nota3 = int(input("Digite a 3ª nota: "))

    print(f"A média de notas é {calcular_media(nota1, nota2, nota3):.2f}")
    
    print()

def q2():
    print("-----  Questāo 2  -----")
    numero = int(input("Digite um número: "))
    print(f"O número de pares de 0 até {numero} é: {contar_pares(numero)}") 
    
    print()

def q3():
    print("-----  Questāo 3  -----")
    print("Coletando um número aleatório de 1 a 100!")
    numero = gera_n()
    multiplos_3 = [multiplo_3 for multiplo_3 in range(1, numero + 1) if(multiplo_3 % 3 == 0)]
    multiplos_5 = [multiplo_5 for multiplo_5 in range(1, numero + 1) if(multiplo_5 % 5 == 0)]
    soma = 0
    for multiplo in multiplos_3:
        soma += multiplo
    for multiplo in multiplos_5:
            soma += multiplo

    multiplos = []
    multiplos.extend(multiplos_3)
    multiplos.extend(multiplos_5)
    multiplos.sort()
    multiplos = [str(x) for x in multiplos]

    print(f"O número gerado foi {numero}, os multiplos são: {', '.join(multiplos)} cuja soma é: {soma}")
    
    print()

def q4():
    print("-----  Questāo 4  -----")
    print("-----  Calculadora  -----")
    n1 = int(input("Digite o 1º número: "))
    n2 = int(input("Digite o 2º número: "))
    op = input("Digite a operação (+, -, *, /): ")

    print(f"O resultado é: {calculadora(n1, n2, op)}")
    
    print()

def q5():
    print("-----  Questāo 5  -----")
    entrada = input("Digite os números separados por espaço: ")
    numeros = [float(x) for x in entrada.split()]

    print(f"O resultado é:\n{estatisticas(*numeros)}")

    print()
    


def main():
    q1()
    q2()
    q3()
    q4()
    q5()

if(__name__ == '__main__'):
    q5()