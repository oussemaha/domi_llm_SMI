from flask import Blueprint,request
from .Db_repository import DB_Sqlite3

db_api = Blueprint('db_api', __name__)
db = DB_Sqlite3()

@db_api.route('/', methods=["GET"])
def select():
    return db.select_Table("routing_tab", ["*"])

@db_api.route("/",methods=["POST"])
def add():
    if ("{data}" in request.form.get('question')):
        if (db.select_where("routing_tab", ["route"], ["route='"+request.form.get('route')+"'"])==[]):     
            db.insert("routing_tab", ["route", "question"], [request.form.get('route'), request.form.get('question')])
            return "Route added", 200
        else:
            return "Route already exists", 400
    else:
        return "Question should contain {data} placeholder", 400

@db_api.route("/<path:subpath>",methods=["DELETE"])
def delete(subpath):
    if (db.select_where("routing_tab", ["route"], ["route='"+subpath+"'"])==[]):     
        return "Route not found", 404
    else:
        db.delete("routing_tab", ["route='"+subpath+"'"])
        return "Route deleted", 200

@db_api.route("/<path:subpath>",methods=["PUT"])
def update(subpath):
    if (db.select_where("routing_tab", ["route"], ["route='"+subpath+"'"])==[]):     
        return "Route not found", 404
    else:
        db.update("routing_tab", ["question"], [request.form.get('question')], "route='"+subpath+"'")
        return "Route updated", 200