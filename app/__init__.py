from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app= Flask(__name__)
api=Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///crud.db'
db= SQLAlchemy(app)
from app.models.missoes import Missions
with app.app_context():
    db.create_all()
from app.view.reso_missions import Index
api.add_resource(Index,"/")
from app.view.reso_missions import MissionCreate
api.add_resource(MissionCreate,"/create")
#@app.route("/")
#def index():
#    return render_template('/index.html')'''