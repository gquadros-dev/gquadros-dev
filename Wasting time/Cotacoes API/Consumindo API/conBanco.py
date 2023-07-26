import psycopg2

class Conexao:
    def __init__(self):
        self.host = "localhost",
        self.database = "postgres",
        self.user = "postgres",
        self.password = "20023107"

    def criarConexao(self):
        con = psycopg2.connect(host =self.host, database = self.database, user = self.user, password = self.password)
        return con

    def criaCursor(self, con):
        return con.cursor()

