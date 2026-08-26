
def q1():
    print("-----  Questāo 1  -----")
    comando = aluno_maior_nota =''
    maior_nota = nota = 0.0
    while(comando != 'exit'):
        comando = input('Digite o nome do aluno (exit para sair): ')
        if(comando == 'exit'):
            break
        nota = float(input('Digite a nota do aluno (-1 para sair): '))
        if(nota == -1):
            break

        if(nota > maior_nota):
            maior_nota = nota
            aluno_maior_nota = comando

    print(f"O aluno com maior nota é {aluno_maior_nota}, sua nota é: {maior_nota:.2f}")
    print("\n")

def q2():
    print("-----  Questāo 2  -----")
    texto = input('Informe o texto: ')
    texto = texto.replace('banana', 'Maçā')
    print('Novo texto:')
    print(texto)
    print("\n")

def q3():
    print("-----  Questāo 3  -----")
    texto = input('Informe o texto: ')
    texto = texto.replace('a', 'A')
    texto = texto.replace('e', 'A')
    texto = texto.replace('i', 'A')
    texto = texto.replace('o', 'A')
    texto = texto.replace('u', 'A')
    print('Novo texto:')
    print(texto)
    print("\n")

def q4():
    print("-----  Questāo 4  -----")
    user = input('Informe o nome de usuário: ')
    user = user[::-1]
    print(f'O nome de usuário de trás para frente é: {user}')

    print("\n")

def q5():
    print("-----  Questāo 5  -----")
    texto = input('Informe o texto: ')
    letra = input('Informe a letra a ser contada: ')
    
    print(f"A letra '{letra}' aparece {texto.count(letra)} no texto!")

    print("\n")

def main():
    q1()
    q2()
    q3()
    q4()
    q5()

if(__name__ == '__main__'):
    q5()