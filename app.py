from flask import Flask, render_template, request, redirect,flash
from DAO import *

app = Flask(__name__)
app.secret_key = 'dados'

# Criando o Método para chamar a Tela Principal do Projeto
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro")
def formulario():
    return render_template('formulario.html')

@app.route('/cadastrar', methods=['POST'])
def rota_cadastrar_produto():
    nome:str = request.form['nome']
    codigo:str = request.form['codigo']
    descricao:str = request.form['descricao']
    valor_produto:float = request.form['valor-produto']
    valor_revenda: float = request.form['valor-revenda']
    unidade:str = request.form['unidade']
    quantidade:int = request.form['quantidade']
    imagem:str = request.form['imagem']
    
    cadastrar_produto(nome_produto=nome,codigo_produto=codigo,descricao=descricao,valor_produto=valor_produto,
                      valor_revenda=valor_revenda,unidade=unidade,quantidade=quantidade,imagem=imagem)
    
    flash("✅ Produto cadastrado com sucesso!")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)