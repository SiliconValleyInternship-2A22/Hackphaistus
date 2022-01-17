#import face_alignment
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import io
import collections
from connection import s3_connection

# def main(url):
#     # Optionally set detector and some additional detector parameters
#     face_detector = 'sfd'
#     face_detector_kwargs = {"filter_threshold" : 0.8}
#     # Run the 3D face alignment on a test image, without CUDA.
#     fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, device='cpu', flip_input=True,face_detector=face_detector, face_detector_kwargs=face_detector_kwargs)
#     # AWS S3 bucket
#     #s3 = s3_connection()
#     # 버켓이름,버켓하위 경로를 포함한 s3속 파일명,로컬에 저장할때 파일명
#     #s3.download_file(url[0],url[1],url[2])
#     # try:
#     #     input_img = io.imread(url[2])
#     # except FileNotFoundError:
#     #     input_img = io.imread(url[2])
#     input_img = io.imread('/static/img/pil.jpg')
#     preds = fa.get_landmarks(input_img)[-1]

#     # 2D-Plot
#     plot_style = dict(marker='o',markersize=1,linestyle='-',lw=2)
#     pred_type = collections.namedtuple('prediction_type', ['slice', 'color'])
#     pred_types = {'face': pred_type(slice(0, 17), (0.682, 0.780, 0.909, 0.5)),
#               'eyebrow1': pred_type(slice(17, 22), (1.0, 0.498, 0.055, 0.4)),
#               'eyebrow2': pred_type(slice(22, 27), (1.0, 0.498, 0.055, 0.4)),
#               'nose': pred_type(slice(27, 31), (0.345, 0.239, 0.443, 0.4)),
#               'nostril': pred_type(slice(31, 36), (0.345, 0.239, 0.443, 0.4)),
#               'eye1': pred_type(slice(36, 42), (0.596, 0.875, 0.541, 0.3)),
#               'eye2': pred_type(slice(42, 48), (0.596, 0.875, 0.541, 0.3)),
#               'lips': pred_type(slice(48, 60), (0.596, 0.875, 0.541, 0.3)),
#               'teeth': pred_type(slice(60, 68), (0.596, 0.875, 0.541, 0.4))
#               }

#     fig = plt.figure(figsize=plt.figaspect(.5))
#     ax = fig.add_subplot(1, 2, 1)
#     ax.imshow(input_img)
#     for pred_type in pred_types.values():
#         ax.plot(preds[pred_type.slice, 0],
#                 preds[pred_type.slice, 1],
#                 color=pred_type.color, **plot_style)
#     #ax.axis('off')
#     plt.savefig(url[2]) # 사진 점선만

# # 3D-Plot
#     ax = fig.add_subplot(1, 2, 2, projection='3d')
#     #surf = ax.scatter(preds[:, 0] * 1.2,preds[:, 1],preds[:, 2],c='cyan',alpha=1.0,edgecolor='b')
#     featureName = []
#     featureX = []
#     featureY = []
#     for pred_type in pred_types.values():
#         ax.plot3D(preds[pred_type.slice, 0] * 1.2,preds[pred_type.slice, 1],preds[pred_type.slice, 2], color='blue')
#         fes = [k for k, v in pred_types.items() if v == pred_type]
#         featureName.append(fes[0])

#         tmp = []
#         for i in preds[pred_type.slice, 0] * 1.2:
#             tmp.append(round(i,2)) # 소숫점 반올림 일단은...!  소숫점 둘째 자리는 tmp.append(round(i,2))
#         featureX.append(tmp)
#         tmp = []
#         for i in preds[pred_type.slice, 1]:
#             tmp.append(round(i,2)) # 소숫점 반올림 일단은...!  소숫점 둘째 자리는 tmp.append(round(i,2))
#         featureY.append(tmp)    
#     result = [featureName,featureX,featureY]
#     print(result)
#     #plt.show()
#     #os.remove(url[2])
#     #plt.savefig(url[2])  # 전체 저장
#     return result