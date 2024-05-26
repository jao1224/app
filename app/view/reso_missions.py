from app.models.missoes import Missions
from flask import jsonify, request
from flask_restful import Resource, reqparse
from datetime import datetime



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
argumentos_update.add_argument('id', type=int)
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

#pesquisar por id 
argumentos_pesquisa=reqparse.RequestParser()
argumentos_pesquisa.add_argument('id', type=int)
#pesquisa por data 
argumentos_pesquisadt=reqparse.RequestParser()
argumentos_pesquisadt.add_argument('data_lancamento', type=str)
#pesquisa por data mas por ordem decrescente
argumentos_pesquisa_orden=reqparse.RequestParser()
argumentos_pesquisa_orden.add_argument('data_lancamento', type=str)


class Index(Resource):
    def get(self):
        return jsonify("Bem-vindo à aplicação Flask")

# Criar (POST)
class Mission_Create(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            data_lancamento = datetime.strptime(datas['data_lancamento'], '%Y-%m-%d %H:%M:%S')
        
            duracao = datetime.strptime(datas['duracao'], '%Y-%m-%d %H:%M:%S')
        
            Missions.save_missions(
                self,
                nome=datas['nome'],
                data_lancamento=data_lancamento,
                destino=datas['destino'],
                estado=datas['estado'],
                tripulacao=datas['tripulacao'],
                carga_util=datas['carga_util'],
                duracao=duracao,
                custo=datas['custo'],
                status=datas['status']
            )
            return {"message": "Missão foi adicionada com sucesso"},200
        except Exception as e:
            return jsonify({"error":str(e)})

# Update
class Mission_update(Resource):
    def put(self):
        try:
            
            datas = argumentos_update.parse_args()
            data_lancamento = datetime.strptime(datas['data_lancamento'], '%Y-%m-%d %H:%M:%S')
        
            duracao = datetime.strptime(datas['data_lancamento'], '%Y-%m-%d %H:%M:%S')
        
            
            Missions.update_mission(
                self,
                id=datas['id'],
                nome=datas['nome'],
                data_lancamento=data_lancamento,
                destino=datas['destino'],
                estado=datas['estado'],
                tripulacao=datas['tripulacao'],
                carga_util=datas['carga_util'],
                duracao=duracao,
                custo=datas['custo'],
                status=datas['status']
            )
            return ("Missão foi atualizada com sucesso")
        except Exception as e:
            return jsonify({"error":str(e)})

# Deletar
class Mission_Delete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            Missions.delete_mission(self,datas['id'])
            return ("Missão foi deletada com sucesso")
        except Exception as e:
            return jsonify({"error":str(e)})
        
        
    # Recuperar os detalhes de uma missão específica com base no ID da missão
class Mission_id(Resource):
    def get(self):
        try:
            datas = argumentos_pesquisa.parse_args()
            missao=Missions.get_mission_by_id(self,datas['id'])
            if missao:
                return missao
            return{"message": 'Missão não encontrada !'},200
        except Exception as e:
            return jsonify({'status': 500, 'msg':f'{e}'}),500
            
        
        
# Pesquisar missões por intervalo de datas
class Missions_interval(Resource):
    def get(self):
    
        try:
            datas = argumentos_pesquisadt.parse_args()
            data_inicial = datetime.strptime(datas['data_lancamento'], '%Y-%m-%d %H:%M:%S')
            data_final = datetime.strptime(datas['data_lancamento'], '%Y-%m-%d %H:%M:%S')
            missao=Missions.get_missions_by_date_range(self,data_inicial,data_final)
            if missao:
                # Certifique-se de que 'missao' seja serializável em JSON
                return jsonify(missao)
            return jsonify({'Message': "Missao nao encontrada"}), 200
        except Exception as e:
            return jsonify({"error": str(e)})
        
        
#todas as missoes em ordem decrescente 
class Missions_Por_ordem_decrescente(Resource):
    def get(self):
    
        try:
            datas = argumentos_pesquisa_orden.parse_args()
            data_ordenada = datetime.strptime(datas['data_lancamento'], '%Y-%m-%d')
            detalhes_missao=Missions.all_misson(self,data_ordenada)
            if detalhes_missao:

       
                # Retorna os detalhes das missões em formato JSON
                return jsonify(detalhes_missao)
            else:
                return jsonify({'Message': "Missao nao encontrada"}), 404

        except Exception as e:
            return jsonify({"error": str(e)})



            