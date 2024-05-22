from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app= Flask(__name__)
api=Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mission.db'
db= SQLAlchemy(app)
from app.models.missoes import Missions
with app.app_context():
    db.create_all()
from app.view.reso_missions import Index, Mission_Create, Mission_update,Mission_Delete,Mission_por_id,Missions_Por_intervalo
api.add_resource(Index,"/")
api.add_resource(Mission_Create,'/Create')
api.add_resource(Mission_update,'/Update')
api.add_resource(Mission_Delete,'/Delete')
api.add_resource(Mission_por_id,'/id')
api.add_resource(Missions_Por_intervalo,'/data')

#@app.route("/")
#def index():
#    return render_template('/index.html')'''
