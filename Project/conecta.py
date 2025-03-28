import mysql.connector

def conectar():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="teste123",
            database="cadastro"
        )
        return db
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco de dados:", erro)
        return None
