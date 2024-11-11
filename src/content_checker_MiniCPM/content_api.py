from flask import Blueprint, request
import sys
sys.path.append(".")
from src.SQLite_DB.Db_repository import DB_Sqlite3
from src.content_checker_MiniCPM.content_checker_miniCPM import ContentCheckerMiniCPM
import json

CPM_api = Blueprint('CPM_api', __name__)
db= DB_Sqlite3()
MiniCpm = ContentCheckerMiniCPM()


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@CPM_api.route('/', methods=['POST'])
def CPM_default():
    try:
        data = json.loads(request.form.get('data'))
    except:
        return "Data should be in json format", 400

    if 'file' not in request.files:
        return "No file part", 400

    imageFile =request.files['file']
    if imageFile.filename == '':
        return "No selected file", 400

    if not allowed_file(imageFile.filename):
        return "File type not allowed", 400
    
    response,code=MiniCpm.process_data(imageFile,data)

    return response,code

@CPM_api.route('/<path:subpath>', methods=['POST'])
def CPM(subpath):
    questions=db.select_where("routing_tab",["question"],["route='"+subpath+"'"])
    if (questions==[]):
        return "Route not found", 404
    question = questions[0][0]
    try:
        data = json.loads(request.form.get('data'))
    except:
        return "Data should be in json format", 400

    if 'file' not in request.files:
        return "No file part", 400

    imageFile =request.files['file']
    if imageFile.filename == '':
        return "No selected file", 400

    if not allowed_file(imageFile.filename):
        return "File type not allowed", 400
    
    response,code=MiniCpm.process_data(imageFile,data,question)

    return response,code