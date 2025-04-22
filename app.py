import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'japonesa', 'ativo': False}, 
    {'nome': 'Salermo', 'categoria': 'italiana', 'ativo': True},
    {'nome': 'Habibi', 'categoria': 'árabe', 'ativo': False}
]

def exibir_nome_do_programa():
    print("""
    𝑆𝑎𝑏𝑜𝑟 𝐸𝑥𝑝𝑟𝑒𝑠𝑠
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n') 

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    print()

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def finalizar_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando app...')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print(f'{"- Nome".ljust(20)} | {"Categoria".ljust(15)} | Estado')
    print('-' * 50)
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        estado = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{nome.ljust(20)} | {categoria.ljust(15)} | {estado}')
    print()
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def ativar_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
            break

    if not restaurante_encontrado:
        print('Restaurante não encontrado.')
    
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
