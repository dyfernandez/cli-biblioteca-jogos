import sqlite3

def criar_banco():
    conn = sqlite3.connect("jogos.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            genero TEXT,
            data_lancamento TEXT,
            desenvolvedora TEXT,
            horas_jogadas REAL,
            status TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    
criar_banco()