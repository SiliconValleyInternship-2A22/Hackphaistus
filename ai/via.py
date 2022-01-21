from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import pymysql
from connection import s3_connection
from config import BUCKET_NAME, LOCATION
import adrianb
import dlibb
via = Flask(__name__)

# MySQL

# RabbitMQ

# CORS(app)
CORS(via, resources={r'*':{'origins': 'http://localhost:5000'}})

@via.route('/api') # Main
def main():
  return render_template('index.html')

result = []
url = []

print(' [*] Waiting for messages. To exit press CTRL+C')

def setResult(r,filename):
    global result
    result = r
    message = ''
    for i in result:
        message += str(i) + '-'
    message += filename
    # send receive    
    channel.basic_publish(exchange='',routing_key='result_queue',body=message,properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
    print(" [x] Sent %r" % r)

def getResult():
    return result

skills = [50,50,50,50,50,50]
def updateSkills(ratio_idx,num):
    cursor = db.cursor()
    sql = '''
	SELECT wisdom, charming, leadership, passion, socialskill, credit 
    FROM ratio, abilities
	WHERE ratio.id = abilities.ratio_id  and ratio.id = %s and abilities.ratio_type = %s;'''
    cursor.execute(sql,[ratio_idx,num])
    tlist = cursor.fetchall()
    skills[0] += int(tlist[0][0])
    skills[1] += int(tlist[0][1])
    skills[2] += int(tlist[0][2])
    skills[3] += int(tlist[0][3])
    skills[4] += int(tlist[0][4])
    skills[5] += int(tlist[0][5])    

def calculateRatio(url): 
    global skills
    skills=[50,50,50,50,50,50]
    # 탐지 모델
    result = dlibb.main(url) #dlib
    features = result[0]
    C_X = result[1]
    C_Y = result[2]
    face = [features[0],C_X[0],C_Y[0]]
    eyebrow1 = [features[1],C_X[1],C_Y[1]]
    eyebrow2 = [features[2],C_X[2],C_Y[2]]
    nose = [features[3],C_X[3],C_Y[3]]
    nostril = [features[4],C_X[4],C_Y[4]]
    eye1 = [features[5],C_X[5],C_Y[5]]
    eye2 = [features[6],C_X[6],C_Y[6]]
    lips = [features[7],C_X[7],C_Y[7]]
    teeth = [features[8],C_X[8],C_Y[8]]

    # 얼굴너비 - 미간
    # 얼굴너비 위치는 제일 작은 y 값 2개의 x값 
    # 눈 사이 미간은 eye1 x값 제일 끝값 - eye2 x값 제일 짧은 값
    f_f_s = face[1][0] # face - face start
    f_f_e = face[1][16] # face - face end
    e_e_s = max(eye1[1])  # eye - eye start
    e_e_e = min(eye2[1])  # eye - eye end
    face_face_length = (f_f_e -  f_f_s) 
    eye_eye_length = (e_e_e -  e_e_s) 
    num = round((float(face_face_length)/eye_eye_length),1)
    print( "1. 미간 비율 : ", num)
    if num > 3.9:
          num = 3
    elif num < 3.6:
          num = 1
    else:
          num = 2
    updateSkills(1,num)
    print("1번 후 미간 스탯 확인 : ",skills)   

    # 입술너비
    # 윗입술 = lips의 y값 중 min
    # 아랫입술 = lips의 y값 중 max
    tmp = lips[2]
    tmp.sort()
    upper_lips = min(lips[2])
    middle_lips = (tmp[5]+tmp[6])/2
    lower_lips = max(lips[2])
    lengthA = (middle_lips-upper_lips) 
    lengthB = (lower_lips-middle_lips)
    print("3. 윗입술 , 아랫입술 높이 : ", lengthA, lengthB) 
    if lengthA <= lengthB:
        num = 2
    else:
        num = 1
    updateSkills(3,num)
    print("3번 후 입술-스탯 확인: ",skills)    

    
    # 입술 너비 - 턱 너비
    # 입술 양끝 x값 비교
    # 가장 근접한 양볼 측정 (y값 비교)
    lips_s = min(lips[1])
    lips_e = max(lips[1])
    lip_lip_length = (lips_e -  lips_s)
    # 턱을 어떤 기준으로 하면 좋을까... 일단 5번째꺼가 기준으로!
    jaw_jaw_length = face[1][12]-face[1][4]
    num = round((float(jaw_jaw_length)/lip_lip_length),1)
    print("4. 입술너비 비율 : ", num)  
    if num < 2.5: 
        num = 1
    else:
        num = 2
    updateSkills(4,num)
    print("4. 입술너비 스탯 : ", skills)  

    # 눈썹모양
    # 왼쪽 눈썹/오른쪽 눈썹의 평균 가로/세로 길이 비교 x축/y축 평균
    l_eb_x = max(eyebrow1[1]) - min(eyebrow1[1])
    r_eb_x = max(eyebrow2[1]) - min(eyebrow2[1])
    avg_eyebrowX = round(float(l_eb_x+r_eb_x)/2,1)
    l_eb_y = max(eyebrow1[2]) - min(eyebrow1[2])
    r_eb_y = max(eyebrow2[2]) - min(eyebrow2[2])
    avg_eyebrowY = round(float(l_eb_y+r_eb_y)/2,1)
    num = round((float(avg_eyebrowX)/avg_eyebrowY),1)
    print ("5. 눈썹 비율 확인: ", num)       
    if num < 5.2: 
        num = 1
    else:
        num = 2  
    updateSkills(5,num)
    print("5번 후 눈썹 모양 스탯 확인 : ",skills)   



    #result = adrianb.main(url) 
    features = result[0]
    C_X = result[1]
    C_Y = result[2]
    face = [features[0],C_X[0],C_Y[0]]
    eyebrow1 = [features[1],C_X[1],C_Y[1]]
    eyebrow2 = [features[2],C_X[2],C_Y[2]]
    nose = [features[3],C_X[3],C_Y[3]]
    nostril = [features[4],C_X[4],C_Y[4]]
    eye1 = [features[5],C_X[5],C_Y[5]]
    eye2 = [features[6],C_X[6],C_Y[6]]
    lips = [features[7],C_X[7],C_Y[7]]
    teeth = [features[8],C_X[8],C_Y[8]]
    # 인중 - 턱
    #코끝 y축 위치는 'nostril’의 3번째 값 / 윗입술 가운데는 lip y [ ] 에서 4번째 값 
    # 아랫입술,아래턱은 최댓값
    n_l_s = nostril[2][2] # nose - lips start
    n_l_e = lips[2][3]    # nose - upperlips end
    l_c_s = max(lips[2])  # lowerlips - chin start
    l_c_e = max(face[2])  # lowerlips - lips end
    nose_lips_length = (n_l_e -  n_l_s) 
    lips_chin_length = (l_c_e -  l_c_s) 
    num = round(float(lips_chin_length)/nose_lips_length)
    print ("2. 인중-턱 비율 확인: ", num)       
    if num > 3.0: 
        num = 3
    elif num < 2.0:
        num = 1
    updateSkills(2,num)
    print("2번 후 눈썹 모양 스탯 확인 : ",skills)   
    return skills

def callback(ch, method, properties, body):
    message = body.decode()
    print("Received: ",message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    url = message.split("-")
    r = calculateRatio(url)
    setResult(r,url[2])
    
# receive task    
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()   

if __name__=="__main__":
    via.run(host="127.0.0.1", port="5005", debug=True)
'''
1. 미간 비율 :  3.6
1번 후 미간 스탯 확인 :  [56, 53, 51, 52, 52, 50]
3. 윗입술 , 아랫입술 높이 :  31.5 33.5
3번 후 입술-스탯 확인:  [62, 61, 43, 50, 62, 60]
4. 입술너비 비율 :  2.2
4번 후 입술너비 스탯 :  [71, 71, 53, 60, 72, 68]
5. 눈썹 비율 확인:  4.5
5번 후 눈썹 모양 스탯 확인 :  [73, 80, 61, 62, 81, 71]
2. 인중-턱 비율 확인:  2

필 최종 :  [78, 90, 61, 62, 86, 74] - dlib으로만!
도운 최종 : [75, 76, 47, 57, 81, 72] - dlib으로만!
최종 :  [79, 73, 61, 66, 73, 84]
'''