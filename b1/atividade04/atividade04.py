import random

def q1():
    print("-----  Questāo 1  -----")
    print("Vamos cadastrar pessoas (para sair insira N):")

    comando = ''
    pessoas = []

    while True:
        comando = input("Informe o nome: ")
        if(comando == 'N'):
            break
        nome = comando

        comando = input("Informe a idade em anos: ")
        if(comando == 'N'):
            break

        idade = int(comando)

        comando = input("Informe a altura em metros: ")
        if(comando == 'N'):
            break

        altura = float(comando)

        comando = input("É estudante (s p/ sim e n p/ não): ")
        if(comando == 'N'):
            break

        estudante = True if comando == 's' else False

        comando = input("Informe os hobbies separados por virgula: ")
        if(comando == 'N'):
            break

        hobbies = comando.split(',')

        pessoas.append((nome, idade, altura, estudante, hobbies))
        print()

    for pessoa in pessoas:
        print(f"Nome: {pessoa[0]}\n" \
            f"Idade: {pessoa[1]} anos\n" \
            f"Altura: {pessoa[2]:.2f} metros\n" \
            f"É estudante: {estudante}\n" \
            f"Hobbies: {','.join(hobbies)}\n")
        print()
    
    print()

def q2():
    print("-----  Questāo 2  -----")
    lista = []

    for i in range(5):
        lista.append(random.randint(0, 100))

    print(f"A lista criada foi {lista}")
    print(f"A lista invertida é {lista[::-1]}")
    
    print()

def q3():
    print("-----  Questāo 3  -----")
    print("Vamos coletar 10 números, insira os números um a um:")
    lista = []

    for i in range(10):
        lista.append(int(input(f"Insira o {i+1}º número: ")))

    pares = [x for x in lista if x % 2 == 0]

    if(pares):
        print(f"O maior número par digitado foi {max(pares)}")
    else:
        print("Não foram digitados números pares")

    print()

def q4():
    print("-----  Questāo 4  -----")
    print("Vamos coletar 10 números, insira os números um a um:")
    lista = []

    for i in range(10):
        lista.append(int(input(f"Insira o {i+1}º número: ")))

    pares = [x for x in lista if x % 2 == 0]

    if(pares):
        print(f"O maior número par digitado foi {max(pares)}")
    else:
        print("Não foram digitados números pares")
        return


    for i in range(max(pares), min(pares) -2, -2):
        print(i)

    print()


def main():
    q1()
    q2()
    q3()
    q4()

if(__name__ == '__main__'):
    main()