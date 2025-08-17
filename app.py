# app.py (código Flask atualizado)
from flask import Flask, request, jsonify, render_template
from connection import connection_db
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar_aluno():
    dados = request.json
    nome = dados.get('nome')
    rga = dados.get('rga')
    
    if not nome or not rga:
        return jsonify({'mensagem': 'Nome e RGA são obrigatórios'}), 400

    try:
        with connection_db() as connection_obj:
            with connection_obj.cursor() as cursor:
                cursor.execute("INSERT INTO alunos VALUES(%s,%s)",(nome,rga))
            connection_obj.commit()
        return jsonify({'mensagem': 'Aluno cadastrado com sucesso'}), 201
    except:
        return jsonify({'mensagem': 'Aluno com este RGA já existe'}), 409

@app.route('/consultar', methods=['POST'])
def consultar_aluno():
    dados = request.json
    rga = dados.get('rga')
    try:
        with connection_db() as connection_obj:
            with connection_obj.cursor() as cursor:
                cursor.execute("SELECT * FROM alunos WHERE rga = %s",(rga,))
                aluno = cursor.fetchone()
        aluno = {"nome": aluno[0],"rga":aluno[1]}
        return jsonify(aluno), 200
    except:
        return jsonify({'mensagem': 'Aluno não encontrado'}), 404
        

@app.route('/mostrar_tudo', methods=['GET'])
def mostrar_tudo():
    try:
        with connection_db() as connection_obj:
            with connection_obj.cursor() as cursor:
                cursor.execute("SELECT * FROM alunos")
                alunos = cursor.fetchall()
        alunos1 = []
        for i in alunos:
            alunos1.append({"nome":i[0],"rga":i[1]})
    except:
        pass
    return jsonify(alunos1), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
