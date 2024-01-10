from flask import Flask, render_template, request, jsonify
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

def conectar_bd():
    return psycopg2.connect(
        host=os.getenv('monorail.proxy.rlwy.net'),
        user=os.getenv('root'),
        password=os.getenv('BF6a4h1G245addaEGaGABda123D6DaA3'),
        database=os.getenv('railway')
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar_pessoa', methods=['POST'])
def adicionar_pessoa():
    nome = request.form.get('nome')
    idade = request.form.get('idade')

    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (%s, %s)", (nome, idade))

        conexao.commit()
        return jsonify({"mensagem": "Pessoa adicionada com sucesso!"})

    except Exception as e:
        print(e)
        return jsonify({"erro": "Erro ao adicionar pessoa"}), 500

    finally:
        cursor.close()
        conexao.close()

if __name__ == '__main__':
    app.run(debug=True)
