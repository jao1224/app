from sqlalchemy import and_
from sqlalchemy import desc
from app import db

class Missions(db.Model):
    __tablename__ = 'mission'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    data_lancamento = db.Column(db.DateTime)
    destino = db.Column(db.String(120))
    estado = db.Column(db.String(120))
    tripulacao = db.Column(db.String(120))
    carga_util = db.Column(db.String(120))
    duracao = db.Column(db.DateTime)
    custo = db.Column(db.Float)
    status = db.Column(db.Text)




    def __init__(self, nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status):
        self.nome = nome
        self.data_lancamento = data_lancamento
        self.destino = destino
        self.estado = estado
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.duracao = duracao
        self.custo = custo
        self.status = status

    def save_missions(self, nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status):
        try:
            add_banco = Missions(nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status)
            print(add_banco)
            db.session.add(add_banco) #adicionar a instância
            db.session.commit() #confirma
        except Exception as e: 
            print(e)

    def update_mission(self, id, nome, data_lancamento, destino, estado, tripulacao, carga_util, duracao, custo, status):
        try:
            db.session.query(Missions).filter(Missions.id==id).update({
                "id":id,
                "nome": nome,
                "data_lancamento": data_lancamento,
                "destino": destino,
                "estado": estado,
                "tripulacao": tripulacao,
                "carga_util": carga_util,
                "duracao": duracao,
                "custo": custo,
                "status": status
            })
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)

    def delete_mission(self, id):
        try:
            db.session.query(Missions).filter(Missions.id==id).delete()
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)
            
        #pesquisa missao por id     
    def get_mission_by_id(self, mission_id):
        try:
            mission = db.session.query(Missions).filter(Missions.id == mission_id).all()
            mission_dict = [{'id': missions.id, 'nome': missions.nome, 'status': missions.status, "destino":missions.destino,"estado": missions.estado,"tripulacao": missions.tripulacao,"data_lancamento": missions.data_lancamento.strftime('%Y-%m-%d %H:%M:%S'),} for missions in mission]
            return mission_dict
        except Exception as e: #se a operação de salvar falhas, cai na exceção
            print(e)
            

#pesquisa por data da missao
    def get_missions_by_date_range(self, data_inicial, data_final):
        try:
    

            # Consulta as missões cuja data de lançamento está entre data_inicial e data_final
            mission = db.session.query(Missions).filter(and_(Missions.data_lancamento >= data_inicial, Missions.data_lancamento <= data_final)).all()

            # Converte os resultados em um dicionário
            missions_dict = [{
                'data_lancamento': missions.data_lancamento, 
                'nome': missions.nome, 'status': missions.status, 
                "destino":missions.destino,"estado": missions.estado,
                "tripulacao": missions.tripulacao,
                } for missions in mission]

            return missions_dict
        except Exception as e:
            return {"error": str(e)}
        
        
        
        




    def all_misson(self,data_ordenada):
        try:
            # Recupera todas as missões do banco de dados
            missoes = db.session.query(Missions).order_by(desc(Missions.data_lancamento==data_ordenada)).all()

            # Cria uma lista de dicionários com os detalhes de cada missão
            mission_detail = [{'nome': missao.nome,
                                 'destino': missao.destino,
                                 'estado': missao.estado,
                                 'data_lancamento': missao.data_lancamento} for missao in missoes]
            
            return mission_detail
        except Exception as e:
            return {"error": str(e)}