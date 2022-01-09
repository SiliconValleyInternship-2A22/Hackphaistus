# app.py
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql

from connection import s3_connection
from config import BUCKET_NAME, LOCATION
from via import calculateRatio

#Flask 객체 인스턴스 생성
app = Flask(__name__)
# CORS(app)
CORS(app, resources={r'*':{'origins': 'http://localhost:3000'}})
# database 설정파일
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/hackphaistus"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='1234',
                     db='hackphaistus',
                     charset='utf8')

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
    s3.put_object(Bucket = BUCKET_NAME,Body = file,Key = file.filename,ContentType = file.content_type)
    dataUrl = [BUCKET_NAME,filename,filename]
    #s3url = f'https://{BUCKET_NAME}.s3.{LOCATION}.amazonaws.com/{filename}'
    skills = sendToDetect(dataUrl)
    print(skills)
    return jsonify({"skills": skills})
    #return jsonify({"skills":[67, 70, 55, 52, 67, 68]})  
    

# 받은 img 파일 -> Flask -> RabbitMQ (-> Python -> AI -> Python) -> Flask
def sendToDetect(url):
  skills = calculateRatio(url)
  return skills


@app.route("/api/printResult", methods=["POST"])
def printResult():
  if request.method == "POST":
    return 'process'


if __name__=="__main__":
  # host 등을 직접 지정하고 싶다면
  app.run(host="127.0.0.1", port="5000", debug=True)