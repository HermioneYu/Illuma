from flask import Flask, request
import json
import requests
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'docx'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']




@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/text', methods=['POST'])
def register():

    text = request.values.get('txt') # Your form's
    key = 'ef5ef5d34e8666e1f03a9269256ec52b'
    url = "http://api.meaningcloud.com/lang-2.0"

    payload = {'key': key, 'txt': text}
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    data = json.loads(response.text)
    language_list = data['language_list']

    language_type = language_list[0]['name']

    return 'The language of your input is: ' + language_type

@app.route('/uploadfile', methods=['POST'])

def upload():
    upload_file = request.files['doc']
    if upload_file and allowed_file(upload_file.filename):
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], upload_file.filename))

        filename = request.values.get('name')

        url = "http://api.meaningcloud.com/lang-2.0"

        key = 'ef5ef5d34e8666e1f03a9269256ec52b'
        payload = {'key': key, 'doc': filename}
        files = {'doc': open(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename), 'rb')}


        response = requests.request("POST", url, data=payload, files=files)
        data = json.loads(response.text)
        language_list = data['language_list']

        language_type = language_list[0]['name']
        return 'The language of the file is: '+ language_type
    else:
        return 'The format is wrong'




if __name__ == '__main__':
    app.run(debug=True)











