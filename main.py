from cli import adicionar_jogo, listar_jogos, editar_jogos, deletar_jogo, restaurar_jogo

def menu():
    opcoes = {
        '1': ('Adicionar jogo', adicionar_jogo),
        '2': ('Listar jogos', listar_jogos),
        '3': ('Editar jogo', editar_jogos),
        '4': ('Deletar jogo', deletar_jogo),
        '5': ('Restaurar jogo', restaurar_jogo),
        '0': ('Sair', None),
    }
    
    while True:
        print('\n=== Biblioteca de Jogos ===')
        for k, (label, _) in opcoes.items():
            print(f'{k}. {label}')
            
        escolha = input('Escolha uma opção: ').strip()
        
        if escolha == '0':
            print('Saindo....')
            break
        
        elif escolha in opcoes:
            opcoes[escolha][1]()
        
        else:
            print('Escolha invalida')

if __name__ == '__main__':
    menu()