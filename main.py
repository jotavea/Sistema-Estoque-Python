estoque = {}

while True:
    print('\n1 - Entrada de produto')
    print('2 - Saída de produto')
    print('3 - Ver estoque')
    print('4 - Sair')

    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
        produto = input('Produto: ').lower()
        quantidade = int(input('Quantidade de entrada: '))

        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
        print('Estoque atualizado!')

    elif opcao == '2':
        produto = input('Produto: ').lower()
        quantidade = int(input('Quantidade de saída: '))

        if produto in estoque and estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print('Saída registrada!')
        else:
            print('Produtdo inexistente ou estoque insuficiente.')

    elif opcao == '3':
        print('\nEstoque: ')

        if estoque:
            for produto, quantidade in estoque.items():
                print(f'{produto}: {quantidade}')
        else:
            print('Estoque vazio.')

    elif opcao == '4':
        print('Sistema encerrado.')
        break

    else:
        print('Opção inválida.')