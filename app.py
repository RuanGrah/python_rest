from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/livros/<int:id>", methods=["Get"])
def get_livro(id):
    print(" ID Livro " + str(id))
    return jsonify("{'nome': 'livro Python 21 dias}")

@app.route("/livros/<int:id>", methods=["Post"])
def create_livro():
    data = request.get_json
    print(data)
    return jsonify(data)

if __name__ == "__main__": 
    app.run(debug=True)
