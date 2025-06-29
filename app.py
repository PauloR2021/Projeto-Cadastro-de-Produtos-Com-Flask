from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os


#Importando os dados do .Env
load_dotenv()

app = Flask(__name__)

# Configurações do banco a partir do .env
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

mysql = MySQL(app)

# Criando o Método para chamar a Tela Principal do Projeto
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro")
def formulario():
    return render_template('formulario.html')


if __name__ == '__main__':
    app.run(debug=True)