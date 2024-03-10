from flask import Flask, request, jsonify
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "Usuário Não Encontrado!!"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    
    if (type(data.get('age') == "int")):
        user_id = str(uuid.uuid4())
        users[user_id] = data
        return jsonify({"message": "Usuário Cadastrado com Sucesso!!", "user_id": user_id}), 201
    else:
        return jsonify({"error": "A idade deve ser um número inteiro"}), 400

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.json
        users[user_id] = data
        return jsonify({"message": "Usuário Atualizado com Sucesso!!"}), 200
    else:
        return jsonify({"error": "Usuário Não Encontrado!!"}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id): 
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "Usuário Deletado com Sucesso!!"}), 200
    else:
        return jsonify({"error": "Usuário Não Encontrado!!"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
