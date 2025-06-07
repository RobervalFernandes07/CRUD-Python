#!/usr/bin/env python3
from conecta import conectar

print("Content-type: text/html\n")  # Cabeçalho HTTP obrigatório

def login():
    try:
        # Obter dados do formulário
        form = cgi.FieldStorage()
        email = form.getvalue('email')
        senha = form.getvalue('senha')
        
        # Conectar ao banco
        db = conectar()
        if db is None:
            print("<h1>Erro ao conectar ao banco</h1>")
            return
            
        cursor = db.cursor()
        
        # Verificar credenciais (NUNCA armazene senhas em texto claro!)
        cursor.execute("SELECT * FROM cliente WHERE email=%s AND senha=%s", (email, senha))
        usuario = cursor.fetchone()
        
        if usuario:
            # Login bem-sucedido - redirecionar para área restrita
            print("""
            <!DOCTYPE html>
            <html>
            <head>
                <meta http-equiv="refresh" content="0;url=area_restrita.html">
            </head>
            <body>
                <p>Login bem-sucedido! Redirecionando...</p>
            </body>
            </html>
            """)
        else:
            # Credenciais inválidas
            print("""
            <script>
                alert("Email ou senha incorretos!");
                window.history.back();
            </script>
            """)
            
    except Exception as e:
        print(f"<h1>Erro: {str(e)}</h1>")
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

if __name__ == "__main__":
    login()