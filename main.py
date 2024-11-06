#from content_checker_GPT.content_checker import gpt_api
from content_checker_MiniCPM.content_checker_miniCPM import load_CPM, minicpm_api
import base64
#from stamp_checker.stamp_checker import stamp_matching

import base64
from flask import Flask,request
import json
from threading import Thread

API_KEY=""
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
model=""
tokenizer=""

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
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
@app.route('/minicpm',methods=['POST'])
def minicpm():
    code =200
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
    response,code=minicpm_api(encoded_image,data,model,tokenizer)
    
    return response,code
@app.route('/minicpm',methods=['GET'])
def minicpm_get():
    return "Please use POST method", 400
    



if __name__=="__main__":
    model, tokenizer = load_CPM()
    """
    if API_KEY=="":
        with open('configs/api_key.txt','r') as f:
            API_KEY=f.read()
    """
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)