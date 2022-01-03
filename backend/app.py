# app.py
from flask import Flask, render_template
from flask_cors import CORS

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

@app.route("/api/fileUpload", methods=["POST"]) # img file Upload
def fileUpload():
    if request.method == "POST":
        # 파일이 존재하지 않을 경우
        # if "file" not in request.files:
        #     flash("no file part")
        #     return redirect(request.rul)

        imgFile = request.files["file"]
        global imgFileName
        imgFileName = secure_filename(imgFile.filename)
        path = os.path.join(Upload_URL, imgFileName)

        return jsonify({"success": True, "file": "Received", "name": filename})  

# 받은 img 파일 -> Flask -> RabbitMQ -> AI -> Flask
def calculateRatio():
  return 0


@app.route("/api/printResult", methods=["POST"])
def printResult():
  abilities = "xxx"
  if request.method == "POST":
    abilities = "abc"
  return abilities


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

@app.route('/home')
def home():
    return render_template('home.html')
    
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