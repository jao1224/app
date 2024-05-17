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
            
    