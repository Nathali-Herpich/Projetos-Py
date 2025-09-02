agenda = {}

def adicionar_Contato():
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    agenda[nome] = telefone
    print(f'Contato {nome} adicionado com sucesso!\n')

def listar_Contatos():
    if not agenda:
        print('Nenhum contato foi adicionado.')
    else:
        print('\n ====== Lista de Contatos: ======')
        for nome, telefone in agenda.items():
            print(f'Nome: {nome}\nTelefone: {telefone}')
            print()

def procurar_Contato():
    nome = input('Digite o nome do contato: ')
    if nome in agenda:
        print(f'{nome} : {agenda[nome]}')
    else:
        print('Contato não encontrado')


while True:
    print('\n===== Menu da Agenda =====')
    print('1 - Adicionar Contato')
    print('2 - Listar Contatos')
    print('3 - Procurar Contato')
    print('4 - Sair da Agenda')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        adicionar_Contato()
    elif opcao == '2':
        listar_Contatos()
    elif opcao == '3':
        procurar_Contato()
    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print(' Erro! Opção inválida!')

