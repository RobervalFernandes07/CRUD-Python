from conecta import conectar

def login():
    db = conectar
    if db is None:
        return
    
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cliente WHERE email=%s AND senha=%s" ,(email, senha))
    usuario = cursor.fetchone()
    
    if usuario:
        print("Login bem sucedido ! ")
    else:
        print("Email ou senha incorretos !!!")
        
    cursor.close()
    db.close()
    
if __name__ == "__main__":
    login() 
    