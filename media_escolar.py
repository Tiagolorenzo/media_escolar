'''Crie um programa que cadastre o nome de 30 alunos em uma lista, e receba de cada aluno 5 notas de 0 a 10. O programa deverá retornar a média do aluno e indicar se o aluno está aprovado ou reprovado (média para aprovação = 7). Ao final, o programa deverá mostrar uma lista com o nome dos aprovados.
'''

# Função para calcular a média de uma lista de notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para determinar se o aluno está aprovado
def verificar_aprovacao(media):
    return media >= 7

# Função para exibir o menu principal
def exibir_menu():
    print('\nMenu:')
    print('1. Cadastrar alunos e notas')
    print('2. Exibir lista de aprovados')
    print('3. Sair do programa')

# Função principal do programa
def programa_principal():
    alunos = []
    aprovados = []

    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')

        match opcao:
            case '1':
                for i in range(30):
                    nome = input(f'Digite o nome do aluno {i + 1}: ')
                    notas = []
                    for j in range(5):
                        while True:
                            try:
                                nota = float(input(f'Digite a nota {j + 1} do aluno {nome} (0 a 10): '))
                                if 0 <= nota <= 10:
                                    notas.append(nota)
                                    break
                                else:
                                    print('Nota inválida. Digite uma nota entre 0 e 10.')
                            except ValueError:
                                print('Entrada inválida. Digite um número.')

                    media = calcular_media(notas)
                    alunos.append({'nome': nome, 'media': media})
                    if verificar_aprovacao(media):
                        aprovados.append(nome)

                print('Alunos cadastrados e notas recebidas com sucesso.')
            case '2':
                if aprovados:
                    print('\nLista de Alunos Aprovados:')
                    for nome in aprovados:
                        print(nome)
                else:
                    print('Nenhum aluno aprovado.')
            case '3':
                print('Saindo do programa.')
                break
            case _:
                print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    programa_principal()


