#from src.content_checker_GPT.content_checker import gpt_api
#from src.content_checker_MiniCPM.content_checker_miniCPM import ContentCheckerMiniCPM
from content_checker_MiniCPM.content_api import CPM_api 

from  SQLite_DB.Db import DB_Sqlite3
from  SQLite_DB.db_api import db_api

import base64


import base64
from flask import Flask,request, Blueprint
import json
from threading import Thread

API_KEY=""
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


Database = DB_Sqlite3()
#MiniCpm=ContentCheckerMiniCPM(miniCPM_model_path)

app = Flask(__name__)
app.register_blueprint(db_api,url_prefix='/db')
app.register_blueprint(CPM_api,url_prefix='/cpm')



#API test
@app.route('/test')
def test():
    return "Server is running",200

#DB test
@app.route('/db_test')
def db_test():
    return str(Database.select_Table("routing_tab",["route","question"])),200



if __name__=="__main__":

    #MiniCpm.load_CPM(miniCPM_model_path)
    Database.create_table("routing_tab",["route unique","question"])

    app.run(host='0.0.0.0',port=5000)

    #run in prod mode
    """
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    """