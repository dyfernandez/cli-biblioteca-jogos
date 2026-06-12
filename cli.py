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
    
adicionar_jogo()