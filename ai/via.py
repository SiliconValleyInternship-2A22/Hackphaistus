import pymysql
import detectLandmarks
import pika
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='hackphaistus',
                     charset='utf8')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
url = []
result = []
print(' [*] Waiting for messages. To exit press CTRL+C')


def setResult(r):
    global result
    result = r

def getResult():
    return result

def callback(ch, method, properties, body):
    message = body.decode()
    print("너 받은 거 맞아?",message)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    url = message.split("-")
    r = calculateRatio(url)
    setResult(r)
    
def checkRabbitMQ():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()   

def calculateRatio(url): 
    skills = [50,50,50,50,50,50]
    # 탐지 모델 
    result = detectLandmarks.main(url) 
    '''
    result = [['face', 'eyebrow1', 'eyebrow2', 'nose', 'nostril', 'eye1', 'eye2', 'lips', 'teeth'], [[385, 397, 410, 437, 475, 514, 566, 631, 734, 
838, 889, 942, 980, 1006, 1032, 1045, 1058], [450, 502, 553, 605, 643], [824, 877, 929, 980, 1019], [734, 734, 748, 748], [683, 708, 734, 773, 799], [527, 566, 605, 643, 605, 566], [838, 877, 916, 954, 916, 864], [618, 656, 708, 734, 760, 812, 851, 812, 773, 734, 696, 656], [631, 708, 734, 773, 838, 773, 734, 708]], [[705, 781, 856, 921, 997, 1051, 1094, 1126, 1148, 1126, 1083, 1051, 986, 910, 856, 
781, 705], [630, 597, 597, 597, 608], [608, 587, 587, 587, 619], [694, 748, 792, 835], [867, 878, 878, 878, 867], [684, 673, 673, 694, 694, 705], [684, 673, 673, 684, 694, 694], [975, 953, 943, 943, 932, 953, 975, 997, 1007, 1007, 1007, 997], [975, 964, 964, 964, 964, 964, 975, 975]]]
    '''
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
    lengthA = abs(f_f_e -  f_f_s) 
    lengthB = (e_e_e -  e_e_s) 
    standard = min(lengthA,lengthB)
    num = round((float(max(lengthA,lengthB))/standard),1)
    #print( "1. 미간 비율 : ", num)
    if num > 3.9:
          num = 3
    elif num < 3.6:
          num = 1
    else:
          num = 2

    cursor = db.cursor()
    sql = '''
	SELECT wisdom, charming, leadership, passion, socialskill, credit 
    FROM ratio, abilities
	WHERE ratio.idx = abilities.ratio_id  and ratio.idx = 1 and abilities.ver = %s;'''
    cursor.execute(sql,[num])
    tlist = cursor.fetchall()
    skills[0] += int(tlist[0][0])
    skills[1] += int(tlist[0][1])
    skills[2] += int(tlist[0][2])
    skills[3] += int(tlist[0][3])
    skills[4] += int(tlist[0][4])
    skills[5] += int(tlist[0][5])
    #print("1번 후 미간 스탯 확인 : ",skills)   


    # 인중 - 턱
    #코끝 y축 위치는 'nostril’의 3번째 값 / 윗입술 가운데는 lip y [ ] 에서 4번째 값 
    # 아랫입술,아래턱은 최댓값
    n_l_s = nostril[2][2] # nose - lips start
    n_l_e = lips[2][3]    # nose - upperlips end
    l_c_s = max(lips[2])  # lowerlips - chin start
    l_c_e = max(face[2])  # lowerlips - lips end
    lengthA = (n_l_e -  n_l_s) 
    lengthB = (l_c_e -  l_c_s) 
    standard = min(lengthA,lengthB)
    num = round(float(max(lengthA,lengthB))/standard)

    #print ("2. 인중-턱 비율 확인: ", num)       

    if num > 3: 
        num = 3
    elif num < 2.0:
        num = 1
    cursor = db.cursor()
    sql = '''
	SELECT wisdom, charming, leadership, passion, socialskill, credit 
    FROM ratio, abilities
	WHERE ratio.idx = abilities.ratio_id  and ratio.idx = 2 and abilities.ver = %s;'''
    cursor.execute(sql,[num])
    tlist = cursor.fetchall()
    skills[0] += int(tlist[0][0])
    skills[1] += int(tlist[0][1])
    skills[2] += int(tlist[0][2])
    skills[3] += int(tlist[0][3])
    skills[4] += int(tlist[0][4])
    skills[5] += int(tlist[0][5])
    #print("2번 후 인중-턱 스탯 확인 : ",skills)   


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
    #print("3. 윗입술 , 아랫입술 높이 : ", lengthA, lengthB) 
    if lengthA <= lengthB:
        num = 2
    else:
        num = 1
    cursor = db.cursor()
    sql = '''
	SELECT wisdom, charming, leadership, passion, socialskill, credit 
    FROM ratio, abilities
	WHERE ratio.idx = abilities.ratio_id  and ratio.idx = 3 and abilities.ver = %s;'''
    cursor.execute(sql,[num])
    tlist = cursor.fetchall()
    skills[0] += int(tlist[0][0])
    skills[1] += int(tlist[0][1])
    skills[2] += int(tlist[0][2])
    skills[3] += int(tlist[0][3])
    skills[4] += int(tlist[0][4])
    skills[5] += int(tlist[0][5])
    #print("3번 후 입술-스탯 확인: ",skills)    

    
    # 입술 너비 - 턱 너비
    # 입술 양끝 x값 비교
    # 가장 근접한 양볼 측정 (y값 비교)
    lips_s = min(lips[1])
    lips_e = max(lips[1])
    lengthA = (lips_e -  lips_s)
    # 턱을 어떤 기준으로 하면 좋을까... 일단 5번째꺼가 기준으로!
    lengthB = face[1][12]-face[1][4]
    #print(lengthA, lengthB)
    standard = min(lengthA,lengthB)
    num = round((float(max(lengthA,lengthB))/standard),1)
    #print("4. 입술너비 비율 : ", num)  
    if num < 2.5: 
        num = 1
    else:
        num = 2       
    cursor = db.cursor()
    sql = '''
	SELECT wisdom, charming, leadership, passion, socialskill, credit 
    FROM ratio, abilities
	WHERE ratio.idx = abilities.ratio_id  and ratio.idx = 4 and abilities.ver = %s;'''
    cursor.execute(sql,[num])
    tlist = cursor.fetchall()
    skills[0] += int(tlist[0][0])
    skills[1] += int(tlist[0][1])
    skills[2] += int(tlist[0][2])
    skills[3] += int(tlist[0][3])
    skills[4] += int(tlist[0][4])
    skills[5] += int(tlist[0][5])
    print("최종 스탯 : ",skills)

    # pil [67, 70, 55, 52, 67, 68]
    
    return skills