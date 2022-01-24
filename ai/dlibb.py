import dlib
from skimage import io
import matplotlib.pyplot as plt
import os
import cv2
from connection import s3_connection
from config import BUCKET_NAME, LOCATION
 
def drawPlot(image,xy,radius,color,thickness):
    image = cv2.circle(image, xy, radius, color, thickness)
    return image

def main(url):
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    s3 = s3_connection()    
    # 버켓이름,버켓하위 경로를 포함한 s3속 파일명,로컬에 저장할때 파일명
    s3.download_file(url[0],url[1],url[2])
    img = dlib.load_rgb_image(url[2])
    #win = dlib.image_window(img, "Image")
    detector = dlib.get_frontal_face_detector()
    faces = detector(img)
    #win.add_overlay(faces) # 얼굴 박스

    #Add plot on the image by using CV2
    path = url[2]
    image = cv2.imread(path)
    print(path)

    featureName = ['face', 'eyebrow1', 'eyebrow2', 'nose', 'nostril', 'eye1', 'eye2', 'lips', 'teeth']
    featureX = []
    featureY = []

    for face in faces:
        landmarks = predictor(img, face)
        parts = landmarks.parts()

        # jaw, ear to ear
        tmpX = []
        tmpY = []
        for part in parts[0:17]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(255,0,0))
            #print("face =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (43,217,250), -1)
            
        '''face = (329, 713) (334, 783) (344, 851) (355, 921) (376, 990) (414, 1049) (469, 1100)(534, 1137)
        (610, 1148)(684, 1135)(746, 1095)(799, 1047)(834, 989)(855, 922)(865, 855)(876, 788)(880, 722)'''
        '''[329, 334, 344, 355, 376, 414, 469, 534, 610, 684, 746, 799, 834, 855, 865, 876, 880]
         [713, 783, 851, 921, 990, 1049, 1100, 1137, 1148, 1135, 1095, 1047, 989, 922, 855, 788, 722]'''
        featureX.append(tmpX)
        featureY.append(tmpY)

        # left eyebrow
        tmpX = []
        tmpY = []
        for part in parts[17:22]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 255, 0))
            #print("left eyebrow =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (215,138,44), -1)
            '''[383, 421, 474, 529, 582] [655, 624, 615, 623, 640]'''
        featureX.append(tmpX)
        featureY.append(tmpY)


        # right eyebrow
        tmpX = []
        tmpY = []
        for part in parts[22:27]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 0, 255))
            #print("right eyebrow =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1])) 
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (153,201,51), -1)
        featureX.append(tmpX)
        featureY.append(tmpY)


        # line on top of nose
        tmpX = []
        tmpY = []
        for part in parts[27:31]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 0, 0))
            #print("nose =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (87,86,254), -1)
        featureX.append(tmpX)
        featureY.append(tmpY)


        # bottom part of the nose
        tmpX = []
        tmpY = [] 
        for part in parts[31:36]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(255, 0, 255))
            #print("nostril =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (87,86,254), -1)
        featureX.append(tmpX)
        featureY.append(tmpY)


        # left eye
        tmpX = []
        tmpY = [] 
        for part in parts[36:42]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(255, 255, 0))
            #print("left eye =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (61, 142, 255), -1)
        featureX.append(tmpX)
        featureY.append(tmpY)

        # right eye
        tmpX = []
        tmpY = [] 
        for part in parts[42:48]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(0, 255, 255))
            #print("right eye =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (61, 142, 255), -1)
        featureX.append(tmpX)
        featureY.append(tmpY)

        # outer part of the lips
        tmpX = []
        tmpY = [] 
        for part in parts[48:60]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(100, 100, 100))
            #print("lips =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (244,244,244), -1)
        featureX.append(tmpX)
        featureY.append(tmpY)


        # inner part of the lips
        tmpX = []
        tmpY = [] 
        for part in parts[60:68]:
            #win.add_overlay_circle(part, 3, dlib.rgb_pixel(255, 255, 255))
            #print("teeth =",part)
            part = str(part)
            part = part[1:-1].split(',')
            tmpX.append(int(part[0]))
            tmpY.append(int(part[1]))
            center_coordinates = (int(part[0]),int(part[1]))
            image = drawPlot(image, center_coordinates, 5, (244,244,244), -1)
        featureX.append(tmpX)
        featureY.append(tmpY)

    result = [featureName,featureX,featureY]
    print(result)
    filename = url[2]+'_result.png'
    cv2.imwrite(filename, image)
    # 이미지 열기
    res = s3.upload_file(filename,BUCKET_NAME,filename)
    os.remove(url[2])
    os.remove(filename)
    #win.wait_until_closed()
    return result