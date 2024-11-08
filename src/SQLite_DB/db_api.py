from flask import Blueprint,request
from .Db import DB_Sqlite3

db_api = Blueprint('db_api', __name__)
db = DB_Sqlite3()

@db_api.route('/select')
def select():
    return db.select_Table("routing_tab", ["*"])

@db_api.route("/add",methods=["POST"])
def add():
        #to add verifiacation on the question, fi it has the parameter {data} 
        if (db.select_where("routing_tab", ["route"], ["route='"+request.form.get('route')+"'"])==[]):     
            db.insert("routing_tab", ["route", "question"], [request.form.get('route'), request.form.get('question')])
            return "Route added", 200
        else:
            return "Route already exists", 400
    