from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app= Flask(__name__)
CORS(app)
api=Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mission.db'
db= SQLAlchemy(app)
from app.models.missoes import Missions
with app.app_context():
    db.create_all()
from app.view.reso_missions import Index, Mission_Create, Mission_update,Mission_Delete,Mission_id,Missions_interval,Missions_decrescente
api.add_resource(Index,"/")
api.add_resource(Mission_Create,'/Create')
api.add_resource(Mission_update,'/Update')
api.add_resource(Mission_Delete,'/Delete')
api.add_resource(Mission_id,'/id')
api.add_resource(Missions_interval,'/date')
api.add_resource(Missions_decrescente,'/all')


#@app.route("/")
#def index():
#    return render_template('/index.html')'''
