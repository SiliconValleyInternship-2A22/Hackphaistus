# app.py
from flask import Flask, request, render_template, jsonify, redirect, url_for
from flask_cors import CORS
from flask_restx import Resource, Api # Swagger
from werkzeug.datastructures import FileStorage
from connection import s3_connection
from config import BUCKET_NAME, LOCATION
from via import *
app = Flask(__name__)
# RabbitMQ

# Swagger API
api = Api(app,version='1.0',title='Hackphaistus API',description='Hackphaistus REST API 문서')
ns = api.namespace('api',description='Hackphaistus API')  
parser = ns.parser()
file_parser = ns.parser()
result_parser = ns.parser()
# CORS(app)
CORS(app, resources={r'*':{'origins': 'http://localhost:3000'}})

result = []
def callback(ch, method, properties, body):
    message = body.decode()
    print("Received: ",message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    arr = message.split("-")
    global result
    for i in range(len(arr)-1):
      result.append(int(arr[i])) 
    channel.close()

@ns.route('/')                 
class Main(Resource):
  def post():
    return render_template('index.html');

@ns.route('/checkCors', methods = ['POST'])        
class setBtn(Resource):
  def post():
    return 'Server has checked your request';

@ns.route('/fileUpload', methods = ['POST'])
class fileUpload(Resource):
  file_parser.add_argument('file',type=FileStorage,required=True,location='files' ,help="얼굴 정면 사진 업로드")  

  @ns.expect(file_parser)
  @ns.response(201, "사진 등록 성공")
  @ns.response(400, "잘못된 요청")
  @ns.response(500, "서버에서 에러 발생")

  def post(self):
    args = file_parser.parse_args()
    global file
    file = args['file']
    filename = file.filename
    # AWS S3 bucket
    s3 = s3_connection()
    s3.put_object(Bucket = BUCKET_NAME,Body = file,Key = file.filename,ContentType = file.content_type)
    dataUrl = BUCKET_NAME+"-"+filename+"-"+filename
    s3url = f'https://{BUCKET_NAME}.s3.{LOCATION}.amazonaws.com/{filename}'
    sendToDetect(dataUrl)
    return result
    
# 받은 img 파일 -> Flask -> RabbitMQ (-> Python -> AI -> Python) -> Flask
def sendToDetect(url):
  message = str(url)
  if not channel.is_open:
    channel.open()
  channel.basic_publish(exchange='',routing_key='task_queue',body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
  print(" [x] Sent %r" % message)

  channel.basic_qos(prefetch_count=1)
  print('rabbitmq:1')
  channel.basic_consume(queue='result_queue', on_message_callback=callback)
  print('rabbitmq:2')
  channel.start_consuming()   
  global result
  print(result)

@ns.route('/printResult')
class printResult(Resource):
  @ns.expect(result_parser)
  @ns.response(201, "스탯 정보 가져옴")
  @ns.response(400, "잘못된 요청")
  @ns.response(500, "서버에서 에러 발생")
  def post(self):
    return getResult()
    # return 'Get Result'

if __name__=="__main__":
  app.run(host="127.0.0.1", port="5000", debug=True)
'''
# app.py
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import pymysql
from connection import s3_connection
from config import BUCKET_NAME, LOCATION

#from via import calculateRatio

#Flask 객체 인스턴스 생성ㄴ
app = Flask(__name__)
# CORS(app)
CORS(app, resources={r'*':{'origins': 'http://localhost:3000'}})
# DB
# db = pymysql.connect(host='localhost',
#                      port=3306,
#                      user='root',
#                      passwd='1234',
#                      db='hackphaistus',
#                      charset='utf8')

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
    s3url = f'https://{BUCKET_NAME}.s3.{LOCATION}.amazonaws.com/{filename}'
    #skills = sendToDetect(dataUrl)
    #print(skills)
    #return jsonify({"skills": skills})
    #return jsonify({"skills":[67, 70, 55, 52, 67, 68]})  
    

# 받은 img 파일 -> Flask -> RabbitMQ (-> Python -> AI -> Python) -> Flask
# def sendToDetect(url):
#   skills = calculateRatio(url)
#   return skills


@app.route("/api/printResult", methods=["POST"])
def printResult():
  if request.method == "POST":
    return 'process'


if __name__=="__main__":
  # host 등을 직접 지정하고 싶다면
  app.run(host="127.0.0.1", port="5000", debug=True)
  '''