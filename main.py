#from content_checker_GPT.content_checker import gpt_api
#from content_checker_MiniCPM.content_checker_miniCPM import ContentCheckerMiniCPM
from SQLite_DB.Db import DB_Sqlite3
import base64
#from stamp_checker.stamp_checker import stamp_matching

import base64
from flask import Flask,request
import json
from threading import Thread

API_KEY=""
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
miniCPM_model_path = "./Model"

Database = DB_Sqlite3("test_database.db")
#MiniCpm=ContentCheckerMiniCPM(miniCPM_model_path)
app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


"""
@app.route('/gpt',methods=['POST'])
def gpt():
    print(request)
    stamp_checked=False
    stamp_result=list()
    code = 200
    data = json.loads(request.form.get('data'))
    if type(data)!=dict:
        return "Data should be a json format", 400

    if 'file' not in request.files:
        return "No file part", 400

    f =request.files['file']
    if f.filename == '':
        return "No selected file", 400

    if not allowed_file(f.filename):
        return "File type not allowed", 400
    file_data = f.read()
    encoded_image = base64.b64encode(file_data).decode('utf-8')
    if "stamp" in data:
        t1=Thread(target=stamp_matching,args=(encoded_image,data['stamp'],stamp_result))
        t1.start()
        stamp_checked=True
        data.pop('stamp')
    response,code=gpt_api(encoded_image,data,API_KEY)
    if stamp_checked and code==200:
        t1.join()
        response['stamp']=stamp_result[0]
        
    return response,code
    """
#API test
@app.route('/test')
def test():
    return "Server is running",200

#DB test
@app.route('/db_test')
def db_test():
    Database.insert("test_table",["name","age"],["John",25])
    return str(Database.select_Table("test_table",["name","age"])),200

"""
@app.route('/minicpm',methods=['POST'])
def minicpm():
    code=None
    try:
        data = json.loads(request.form.get('data'))
    except:
        return "Data should be a json format", 400

    if 'file' not in request.files:
        return "No file part", 400

    imageFile =request.files['file']
    if f.filename == '':
        return "No selected file", 400

    if not allowed_file(f.filename):
        return "File type not allowed", 400
    
    response,code=MiniCpm.process_data(imageFile,data)
    return response,code
"""

if __name__=="__main__":
    """
    if API_KEY=="":
        with open('configs/api_key.txt','r') as f:
            API_KEY=f.read()
    """
    #MiniCpm.load_CPM(miniCPM_model_path)
    Database.create_table("test_table",["name unique","age int"])

    app.run(host='0.0.0.0',port=5000)

    #run in prod mode
    """
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    """