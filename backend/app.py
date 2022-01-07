# app.py
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from connection import s3_connection
from config import BUCKET_NAME, LOCATION
import detectLandmarks

#Flask 객체 인스턴스 생성
app = Flask(__name__)
# CORS(app)
CORS(app, resources={r'*':{'origins': 'http://localhost:3000'}})

@app.route('/api') # Main
def main():
  return render_template('index.html');

@app.route('/api/checkCors', methods = ['POST']) # Cors Check
def setBtn():
  return 'Server has checked your request';

@app.route('/api/fileUpload', methods = ['POST']) # img file Upload
def fileUpload():
  if request.method == 'POST':
    global file
    file = request.files['file']
    filename = file.filename
    # AWS S3 bucket
    s3 = s3_connection()
    s3.put_object(Bucket = BUCKET_NAME,Body = file,Key = file.filename,
    	ContentType = file.content_type)
    s3path = "s3://{BUCKET_NAME}/"+filename
    global s3url
    s3url = f'https://{BUCKET_NAME}.s3.{LOCATION}.amazonaws.com/{filename}'
    calculateRatio()
    return jsonify({"success": True, "file": "Received", "name": filename, "path": s3path})  
    

# 받은 img 파일 -> Flask -> RabbitMQ -> AI -> Flask
def calculateRatio():
  result = detectLandmarks.main()
  print(result)
  return 0


@app.route("/api/printResult", methods=["POST"])
def printResult():
  if request.method == "POST":
    return 'process'


if __name__=="__main__":
  # host 등을 직접 지정하고 싶다면
  app.run(host="127.0.0.1", port="5000", debug=True)



'''
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from helloflask.model.user_model import Members

app = Flask(__name__)

# database 설정파일
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/testdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/one")
def home():
	member = Members.query.first()
	return 'Hello {0}, {1}, {2}, {3}, {4}'\
		.format(member.name, member.email, member.phone, member.start.isoformat(), member.end.isoformat())
	#return render_template('home.html')
    
@app.route('/all')
def select_all():
    members = Members.query.all()
    return render_template('db.html', members=members)
'''