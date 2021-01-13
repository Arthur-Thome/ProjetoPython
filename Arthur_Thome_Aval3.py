# Avaliação 3 individual: Lógica de Programação - segunda-feira
# Autor: ARTHUR THOME
# Salve este arquivo com o seu nome .py. Exemplo:  ivoneiMarques.py
#
# Competências a serem avaliadas:
# - Saber interpretar o que foi solicitado.
# - Saber utilizar os comandos vistos em aula corretamente.
# - Conseguir desenvolver uma solução viável para o problema proposto.
# - Códigos iguais: D
# 
''' 
Você deverá criar um programa para executar as opções do menu a abaixo conforme as instruções.
'''

'''

Menu de opções:
========================================================
0- Finalizar o código
1- Cadastrar
2- Alterar
3- Relatório Geral
4- Relatório por Curso
========================================================
Escolha: '''

'''
Instruções:
Na opção 0, você deverá fazer com que o código encerre sua execução
            mostrando a seguinte mensagem: "Programa Finalizado."

Na opção 1, você deverá realizar a digitação dos seguintes dados:
            >Nome           
            >Curso  (aceitar somente um dos cursos da listaDeCursos)

            O nome deverá ser armazenado em listaDeNomes e o curso
            escolhido em listaCursoEscolhido.
            O curso deverá ser um dos seguintes:
            listaDeCursos = ['ADS', 'RDS', 'SPI','MMD', 'Moda']

Na opção 2, você deverá ler o nome de um aluno e alterar o seu curso.
            Escolher apenas um dos cursos da listaDeCursos

Na opção 3, você deverá mostrar o total de alunos e opercentual de
             alunos por curso.
            Exemplo:    Total Geral de Alunos: 985
                        ADS : 29 %
                        RDS : 31 %
                        SPI : 18 %
                        MMD : 12 %
                        Moda: 10 %
                        
Na opção 4, o usuário deverá escolher um curso e visualizar todos
    os alunos do curso escolhido.
    Exemplo:

    Escolha um Curso: RDS
    Curso escolhido: RDS
    Alunos:
    -Pedro 
    -Carlos
    -Mario




listaDeNomes    listaCursoEscolhido
  _________      _____
0| Ana     |   0| ADS |
1| Pedro   |   1| RDS |
2| Carlos  |   2| RDS |
3| Maria   |   3| Moda|
4| João    |   4| SPI |
5| Carla   |   5| ADS |

'''



menu = '''
========================================================
0- Finalizar o código
1- Cadastrar
2- Alterar
3- Relatório Geral
4- Relatório por Curso
========================================================
'''

listaDeNomes = []
listaCursoEscolhido = []
listaDeCursos = ['ADS','RDS', 'SPI','MM', 'Moda']

while True:
    print(menu)
    option = int(input("Escolha uma opção: "))

    if option == 0:
        print("Programa Finalizado.")
        break

    if option == 1:
        listaDeNomes.append(input("Digite seu nome: "))
        print('Tipos de cursos:\n1 - ADS', '\n2 - RDS', '\n3 - SPI','\n4 - MMD', '\n5 - Moda')
        listaCursoEscolhido.append(input("Digite seu curso: "))

    if option == 2:
        aluno = input("Digite o nome do Aluno: ")
        ind = 0
        for nome in listaDeNomes:
            if nome == aluno:
                curso1 = input("Digite o novo curso: ")
                listaCursoEscolhido[ind] = curso1
                break
            ind += 1

    if option == 3: 
        pass

    if option == 4:
        curso = input("Digite um Curso: ")
        ind = 0
        for aluno in listaDeNomes:
            if listaCursoEscolhido[ind] == curso:
                print(" -",aluno)
            ind += 1
            
        
