from flask import Flask, jsonify, request

from conexao import conecta_db

from cadastro_livro import (
    inserir,alterar,deletar,consultar,consultar_por_id
    )

app = Flask(__name__)

@app.route("/livros/<int:id>", methods=["GET"])
def get_livro(id):
    print(" ID Livro " + str(id))
    return jsonify("{'nome': 'livro Python 21 dias}")

@app.route("/livros", methods=["POST"])
def inserir_livro():
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    inserir(conexao,nome)
    print(data)
    return jsonify(data)

@app.route("/livros/<int:id>", methods = ["PUT"])
def alterar_livro(id):
    conexao = conecta_db()
    data = request.get_json()
    nome=data["nome"]
    alterar(conexao,id,nome)
    return jsonify(data)

@app.route("/livros/<int:id>", methods =["DELETE"])
def deletar_livro(id): 
    conexao = conecta_db()
    deletar(conexao,id)


@app.route("/livros", methods=["GET"])
def listar_todos():
    conexao = conecta_db()
    livros = consultar(conexao)
    return jsonify(livros)






if __name__ == "__main__": 
    app.run(debug=True)
