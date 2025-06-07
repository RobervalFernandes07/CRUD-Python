from backend.conecta import conectar

def cadastrar_usuario(dados):
    db = conectar()
    if db is None:
        return 'erro_conexao'

    cursor = db.cursor()
    cursor.execute("SELECT * FROM cliente WHERE email = %s", (dados['email'],))
    if cursor.fetchone():
        return 'email_existente'

    cursor.execute("""
        INSERT INTO cliente (nome, cpf, telefone, idade, email, senha)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        dados['nome'],
        dados['cpf'],
        dados['telefone'],
        dados['idade'],
        dados['email'],
        dados['senha']
    ))
    db.commit()
    cursor.close()
    db.close()
    return 'ok'
