import sqlite3
from game import Jogo


def adicionar_jogo():
    titulo = input("Digite o título do jogo: ")
    generos = ['Ação', 'Aventura', 'RPG', 'Estratégia', 'Simulação', 'Esportes', 'Luta', 'Terror', 'Plataforma']
    for i, g in enumerate(generos, 1): 
        print(f"{i}. {g}")
    genero = generos[int(input("Escolha o número: ")) - 1]
    desenvolvedora = input("Digite a desenvolvedora do jogo: ")
    horas_jogadas = float(input("Digite a quantidade de horas jogadas: "))
    data_lancamento = input("Digite a data de lançamento do jogo: ")
    game_status = ['Não jogado', 'Zerado', 'Jogando','Abandonado']
    for i, s in enumerate(game_status, 1):  
        print(f"{i}. {s}")             
    status = game_status[int(input("Selecione o Status: ")) - 1]
    
    conn = sqlite3.connect('jogos.db')    
    cursor = conn.cursor()
    
    cursor.execute("""
                INSERT INTO jogos (titulo, genero, data_lancamento, desenvolvedora, horas_jogadas, status)
                VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, genero, data_lancamento, desenvolvedora, horas_jogadas, status))
    
    conn.commit()
    conn.close()
    
    print('Jogo adicionado com sucesso!')

def listar_jogos():
    conn = sqlite3.connect('jogos.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM jogos WHERE deletado = 0')
    jogos = cursor.fetchall()
    
    for jogo in jogos:
        print(f'ID: {jogo[0]} | Titulo: {jogo[1]} | Gênero: {jogo[2]} | Data de Lançamento: {jogo[3]} | Desenvolvedora: {jogo[4]} | Horas jogadas: {jogo[5]}h | Status: {jogo[6]}')
    
    conn.close()

def editar_jogos():
    conn = sqlite3.connect('jogos.db')
    cursor = conn.cursor()
    
    listar_jogos()
    id = int(input('Digite o jogo que deseja editar: '))
    
    editgame = ['Titulo', 'Gênero', 'Data de Lançamento', 'Desenvolvedora', 'Horas jogadas', 'Status']
    for i, e in enumerate(editgame, 1):
        print(f'{i}. {e}')
    edit_jogos = editgame [int(input('Selecione o que editar: ') ) - 1]

    colunas = {
        'Titulo': 'titulo',
        'Gênero': 'genero',
        'Data de Lançamento': 'data_lancamento',
        'Desenvolvedora': 'desenvolvedora',
        'Horas jogadas': 'horas_jogadas',
        'Status': 'status'
    }
    if edit_jogos == 'Status':
        game_status = ['Não jogado', 'Zerado', 'Jogado', 'Abandonado']
        for i, s in enumerate(game_status, 1):
            print(f'{i}, {s}')
        novo_valor = game_status [int(input('Selecione o novo Status: ')) -1]    
    elif edit_jogos == 'Gênero':
        generos = ['Ação', 'Aventura', 'RPG', 'Estratégia', 'Simulação', 'Esportes', 'Luta', 'Terror', 'Plataforma']
        for i, g in enumerate(generos, 1): 
            print(f"{i}. {g}")
        novo_valor = generos [int(input('Selecione o novo Gênero: ')) -1]
    else:
        novo_valor = input(f'Digite o novo valor para{edit_jogos}: ')
    
    cursor.execute(f'UPDATE jogos SET {colunas[edit_jogos]} = ? WHERE id = ?', (novo_valor, id) )
    
    conn.commit()
    conn.close()


#listar_jogos()
#adicionar_jogo()
editar_jogos()