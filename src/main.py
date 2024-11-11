
from content_checker_MiniCPM.content_api import CPM_api 

from  SQLite_DB.db_api import db_api

import base64
from flask import Flask,request, Blueprint

API_KEY=""
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



app = Flask(__name__)
app.register_blueprint(db_api,url_prefix='/db')
app.register_blueprint(CPM_api,url_prefix='/cpm')



#API test
@app.route('/test')
def test():
    return "Server is running",200




if __name__=="__main__":


    app.run(host='0.0.0.0',port=5000)

    #run in prod mode
    """
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    """