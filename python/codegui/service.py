from flask import Flask
from flask import request
import os
app = Flask(__name__)
code=''

UPLOAD_FOLDER = '/home/copie/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return code
@app.route('/postcode', methods=['POST', 'GET'])
def postcode():
    global code
    if request.method == "GET":
        code = request.args.get('code', '')
        return '200'
@app.route('/upfile',methods=['POST'])
def upfile():
    if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                # filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], "ehwjfhsgd.txt"))
                return "yes"
            
            return "200"
if __name__ == '__main__':
    app.debug = True 
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(host='0.0.0.0')