# app.py
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flask_restx import Resource, Api # Swagger
from werkzeug.datastructures import FileStorage
import pymysql
# from connection import s3_connection
# from config import BUCKET_NAME, LOCATION
from dotenv import load_dotenv
import os
load_dotenv()
BUCKET_NAME = os.environ.get("BUCKET_NAME")
LOCATION = os.environ.get("LOCATION")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
MYSQL_USER=os.environ.get("MYSQL_USER")
MYSQL_PASSWORD=os.environ.get("MYSQL_PASSWORD")
RABBITMQ_DEFAULT_USER=os.environ.get("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS=os.environ.get("RABBITMQ_DEFAULT_PASS")
import boto3
def s3_connection():
    s3 = boto3.client('s3',aws_access_key_id = AWS_ACCESS_KEY,aws_secret_access_key = AWS_SECRET_KEY)
    return s3
app = Flask(__name__)

# MySQL
db = pymysql.connect(host='db',port=3306,user=MYSQL_USER,passwd=MYSQL_PASSWORD,db='Hackphaistus',charset='utf8')
# RabbitMQ
import pika
import uuid
import time
credentials = pika.PlainCredentials(RABBITMQ_DEFAULT_USER,RABBITMQ_DEFAULT_PASS)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_declare(queue='result_queue', durable=True)
# Swagger API
api = Api(app,version='1.0',title='Hackphaistus API',description='Hackphaistus REST API 문서')
ns = api.namespace('api',description='Hackphaistus API')  
parser = ns.parser()
file_parser = ns.parser()
result_parser = ns.parser()
# CORS(app)
CORS(app, resources={r'*':{'origins': 'http://localhost:3000'}})


class FibonacciRpcClient(object):
  def __init__(self):
    credentials = pika.PlainCredentials(RABBITMQ_DEFAULT_USER,RABBITMQ_DEFAULT_PASS)
    self.connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', credentials))
    self.channel = self.connection.channel()

    result = self.channel.queue_declare(queue='', exclusive=True)
    self.callback_queue = result.method.queue
    self.channel.basic_consume(
          queue=self.callback_queue,on_message_callback=self.on_response,auto_ack=True)
  def on_response(self, ch, method, props, body):
    if self.corr_id == props.correlation_id:
      self.response = body

  def call(self, n):
    self.response = None
    self.corr_id = str(uuid.uuid4())
    self.channel.basic_publish(exchange='',routing_key='rpc_queue',properties=pika.BasicProperties(
                reply_to=self.callback_queue,correlation_id=self.corr_id,),body=str(n))
    time.sleep(5)
    while self.response is None:
      self.connection.process_data_events()
      return self.response

# fibonacci_rpc = FibonacciRpcClient()
# print(" [x] Requesting fib(10)")
# response = fibonacci_rpc.call(10)
# print(" [.] Got %r" % response)



global task_id
task_id = 0

@ns.route('/')                 
class Main(Resource):
  def post():
    return render_template('index.html');

@ns.route('/checkCors', methods = ['POST'])        
class setBtn(Resource):
  def post():
    return 'Server has checked your request';

def callback(ch, method, properties, body):
    message = body.decode()
    print("Received: ",message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    arr = message.split("-")
    result = []
    for i in range(len(arr)-1):
      result.append(int(arr[i])) 
    filename = arr[len(arr)-1]
    print('RE1:',result)
    print('RE1:',filename)
    cursor = db.cursor()
    global task_id
    sql = '''
    INSERT into results(task_id,wisdom,charming,leadership,passion,socialskill,credit,s3url) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'''
    cursor.execute(sql,[task_id,result[0],result[1],result[2],result[3],result[4],result[5],filename])
    #channel.close()

@ns.route('/fileUpload', methods = ['POST'])
class fileUpload(Resource):
  file_parser.add_argument('file',type=FileStorage,required=True,location='files',help="얼굴 정면 사진 업로드")  
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
    Skills, Url = sendToDetect(dataUrl)
    return jsonify({'result':Skills, 'url':Url})
    # global task_id
    # task_id += 1
    # return  jsonify({'task': task_id})

# 받은 img 파일 -> Flask -> RabbitMQ (-> Python -> AI -> Python) -> Flask
def sendToDetect(url):
  message = str(url)
  # send task
  fibonacci_rpc = FibonacciRpcClient()
  print(" [x] Requesting fib(10)")
  response = fibonacci_rpc.call(message)
  print(" [.] Got:",response)
  result = response.decode('utf-8')
  result = result.split('-')
  skills = [int(result[0]),int(result[1]),int(result[2]),int(result[3]),int(result[4]),int(result[5])]
  url = 'https://'+BUCKET_NAME+'.s3.'+LOCATION+'.amazonaws.com/'+result[6]+'_result.png'
  return skills,url
  # channel.basic_publish(exchange='',routing_key='task_queue',body=message,
  #   properties=pika.BasicProperties(
  #       delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
  #   ))
  # print(" [x] Sent %r" % message)  
  #receiveFromDetect()
  

@ns.route('/printResult', methods = ['POST'])
class printResult(Resource):
  result_parser.add_argument('taskID',required=True)  
  @ns.expect(result_parser)
  @ns.response(201, "스탯 정보 가져옴")
  @ns.response(400, "잘못된 요청")
  @ns.response(500, "서버에서 에러 발생")

  def post(self):
    data = request.get_json()
    print(data)
    initID = data['id']
    print(initID)
    ID = int(initID)
    print(ID)
    cursor = db.cursor()
    sql = '''
	  SELECT wisdom, charming, leadership, passion, socialskill, credit, s3url 
    FROM results
	  WHERE task_id = %s;'''
    cursor.execute(sql,[ID])
    tlist = cursor.fetchall()
    result = [int(tlist[0][0]),int(tlist[0][1]),int(tlist[0][2]),int(tlist[0][3]),int(tlist[0][4]),int(tlist[0][5])]
    filename = str(tlist[0][6])
    print(result)
    print(filename)
    s3url = 'https://'+BUCKET_NAME+'.s3.'+LOCATION+'.amazonaws.com/'+filename+'_result.png'
    return jsonify({'file': filename, 'url':s3url,'result':result})


# @ns.route('/receiveSignal', methods = ['POST'])
# class receiveSignal(Resource):
#   def post(self):
#     receiveFromDetect()

# receive result   
# channel.basic_qos(prefetch_count=1)
# channel.basic_consume(queue='result_queue', on_message_callback=callback)
# channel.start_consuming()   

if __name__=="__main__":
  app.run(host="backend", port="5000", debug=True)














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