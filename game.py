class Jogo:
    def __init__(self, titulo, genero, data_lancamento, desenvolvedora, horas_jogadas, status):
        self.titulo = titulo
        self.genero = genero    
        self.data_lancamento = data_lancamento
        self.desenvolvedora = desenvolvedora
        self.horas_jogadas = horas_jogadas
        self.status = status
    
        
    def __str__(self):
        return f"{self.titulo} — {self.genero}, {self.data_lancamento}, {self.desenvolvedora}, {self.horas_jogadas}, {self.status}"
    
jogo = Jogo("Dark Souls", "RPG", "2011-09-22", "FromSoftware", 120, "Zerado")
print(jogo)