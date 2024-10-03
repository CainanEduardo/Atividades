import os

# Inicializando a lista vazia
lista = []

# Menu principal do programa
while True:
    os.system("cls || clear")  # Limpa a tela para melhor visualização

    print('''\nMenu de opções:
    1 - Adicionar um item à lista
    2 - Visualizar lista de itens
    3 - Sair do programa''')
    
    x = int(input('Digite a ação tomada: \n'))
    
    if x == 1:
        # Adicionar um item
        item = input('\nDigite o item que deseja adicionar à lista: ')
        lista.append(item)
        print(f'Item "{item}" adicionado à lista.')
    
    elif x == 2:
        # Visualizar a lista de itens
        if lista == []:
            print('\nA lista está vazia.\n')
        else:
            print('\nItens na lista:')
            for item in lista:
                print(item)
    
    elif x == 3:
        # Sair do programa
        print('Saindo...')
        break
    
    else:
        print('\nOpção inválida, tente novamente.')

    input('\nPressione Enter para continuar...')