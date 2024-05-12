from app.models.missoes import Missions
from flask import jsonify
from flask_restful import Resource, reqparse



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


 #update       
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
class Index(Resource):
    def get(self):
        return jsonify("Bem-vindo à aplicação Flask")

# Criar (POST)
class MissionCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            print(datas)
            missao = Missions(
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
            return ("Missão foi adicionada com sucesso")
        except Exception as e:
            return jsonify({'status': 500, 'msg':f'{e}'}),500
        
        


#update
class Mission_update(Resource):
    def post(self):
        try:
            datas = argumentos_update.parse_args()
            print(datas)
            missao = Missions(
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
            return ("Missão foi adicionada com sucesso")
        except Exception as e:
            return jsonify({'status': 500, 'msg':f'{e}'}),500
        
        
    class MissionDelete(Resource):
        def delete(self, id):
            try:
                Missions.delete_mission(id)
                return ("Missão foi deletada com sucesso")
            except Exception as e:
                return jsonify({'status': 500, 'msg':f'{e}'}),500