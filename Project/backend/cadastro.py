#!/usr/bin/env python3
from conecta import conectar
import cgi
import cgitb; cgitb.enable()  # Para debug

print("Content-type: text/html\n")

# Obter dados do formulário
form = cgi.FieldStorage()

try:
    db = conectar()
    if db is None:
        print("<h1>Erro ao conectar ao banco</h1>")
        exit()

    cursor = db.cursor()

    # Verificar se email já existe
    email = form.getvalue('email')
    cursor.execute("SELECT * FROM cliente WHERE email=%s", (email,))
    
    if cursor.fetchone():
        print("""
        <script>
            alert("Email já cadastrado!");
            window.history.back();
        </script>
        """)
    else:
        # Inserir novo usuário
        cursor.execute(
            "INSERT INTO cliente (nome, cpf, telefone, idade, email, senha) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                form.getvalue('nome'),
                form.getvalue('cpf'),
                form.getvalue('telefone'),
                form.getvalue('idade'),
                email,
                form.getvalue('senha')
            )
        )
        db.commit()
        print("""
        <!DOCTYPE html>
        <html>
        <head>
            <meta http-equiv="refresh" content="0;url=home.html">
        </head>
        <body>
            <p>Cadastro realizado! Redirecionando...</p>
        </body>
        </html>
        """)

except Exception as e:
    print(f"<h1>Erro: {str(e)}</h1>")
finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()