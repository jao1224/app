from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app= Flask(__name__)
api=Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///Missions.db'
db= SQLAlchemy(app)
from app.models.missoes import Missions
with app.app_context():
    db.create_all()
from app.view.reso_missions import Index
api.add_resource(Index,"/")
from app.view.reso_missions import Mission_Create, Mission_update,Mission_Delete
api.add_resource(Mission_Create,"/create")
api.add_resource(Mission_update,"/Update")
api.add_resource(Mission_Delete,"/delete")

#@app.route("/")
#def index():
#    return render_template('/index.html')'''