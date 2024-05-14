from app.models.missoes import Missions
from flask import jsonify
from flask_restful import Resource, reqparse


# Adicionar
argumentos = reqparse.RequestParser()
argumentos.add_argument('nome', type=str)
argumentos.add_argument('data_lancamento', type=str)  
argumentos.add_argument('destino', type=str)
argumentos.add_argument('estado', type=str)
argumentos.add_argument('tripulacao', type=str)
argumentos.add_argument('carga_util', type=str)
argumentos.add_argument('duracao', type=str)  
argumentos.add_argument('custo', type=float)
argumentos.add_argument('status', type=str)

# Update       
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('nome', type=str)
argumentos_update.add_argument('data_lancamento', type=str)  
argumentos_update.add_argument('destino', type=str)
argumentos_update.add_argument('estado', type=str)
argumentos_update.add_argument('tripulacao', type=str)
argumentos_update.add_argument('carga_util', type=str)
argumentos_update.add_argument('duracao', type=str)  
argumentos_update.add_argument('custo', type=float)
argumentos_update.add_argument('status', type=str)

# Deletar
argumentos_delete=reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Bem-vindo à aplicação Flask")

# Criar (POST)
class Mission_Create(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            missao = Missions(
                datas['id'],
                nome=datas['nome'],
                data_lancamento=datas['data_lancamento'],
                destino=datas['destino'],
                estado=datas['estado'],
                tripulacao=datas['tripulacao'],
                carga_util=datas['carga_util'],
                duracao=datas['duracao'],
                custo=datas['custo'],
                status=datas['status']
            )
            missao.save_mission()
            return {"message": "Missão foi adicionada com sucesso"}
        except Exception as e:
            return jsonify({'status': 500, 'msg':f'{e}'}),500

# Update
class Mission_update(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Missions.update_mission(
                datas['id'],
                nome=datas['nome'],
                data_lancamento=datas['data_lancamento'],
                destino=datas['destino'],
                estado=datas['estado'],
                tripulacao=datas['tripulacao'],
                carga_util=datas['carga_util'],
                duracao=datas['duracao'],
                custo=datas['custo'],
                status=datas['status']
            )
            return ("Missão foi atualizada com sucesso")
        except Exception as e:
            return jsonify({'status': 500, 'msg':f'{e}'}),500

# Deletar
class Mission_Delete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            Missions.delete_mission(datas['id'])
            return ("Missão foi deletada com sucesso")
        except Exception as e:
            return jsonify({'status': 500, 'msg':f'{e}'}),500