from flask import Flask, render_template, request, redirect, url_for
from backend import conectar,login,cadastro 

app = Flask(__name__)

@app.route('/')
def pagina_login():
    return render_template('home.html')

@app.route('/cadastro')
def pagina_cadastro():
    return render_template('cadastro.html')

@app.route('/home')
def pagina_home():
    return render_template('home.html')

# adicionar rotas POST para login e cadastro se necessário

if __name__ == '__main__':
    app.run(debug=True)
