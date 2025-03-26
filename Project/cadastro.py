from conecta import conectar

def cadastrar():
    db = conectar()
    if db is None:
        return

    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cursor = db.cursor()

    # Verificar se o email já existe
    cursor.execute("SELECT * FROM cliente WHERE email=%s", (email,))
    usuario_existente = cursor.fetchone()

    if usuario_existente:
        print("❌ Este email já está cadastrado!")
    else:
        # Inserir o novo usuário
        cursor.execute("INSERT INTO cliente (nome,cpf,telefone,idade,email, senha) VALUES (%s, %s,%s,%s,%s,%s)", (nome,cpf,tel,idade,email, senha))
        db.commit()
        print("✅ Cadastro realizado com sucesso!")

    cursor.close()
    db.close()

if __name__ == "__main__":
    cadastrar()
