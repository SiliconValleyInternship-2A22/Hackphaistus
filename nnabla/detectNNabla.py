#@title First let's start by importing dependencies. (double-click to see the codes)
import cv2
import dlib
import nnabla as nn
import nnabla.functions as F
from skimage import io, color
from model import fan, resnet_depth
from external_utils import *
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import collections

#@title Execute Face Detection and FAN. (double-click to see the codes)
from nnabla.ext_utils import get_extension_context
ctx = get_extension_context("cudnn")
nn.set_default_context(ctx)
nn.set_auto_forward(True)

input_img = "/content/pil.jpg"
image = io.imread(input_img)
if image.ndim == 2:
    image = color.gray2rgb(image)
elif image.ndim == 4:
    image = image[..., :3]

face_detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
detected_faces = face_detector(cv2.cvtColor(image[..., ::-1].copy(), cv2.COLOR_BGR2GRAY))
detected_faces = [[d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom()] for d in detected_faces]

if len(detected_faces) == 0:
    print("Warning: No faces were detected.")
    sys.exit()

# Load FAN weights
with nn.parameter_scope("FAN"):
    print("Loading FAN weights...")
    nn.load_parameters("3DFAN4_NNabla_model.h5")

# Load ResNetDepth weights
with nn.parameter_scope("ResNetDepth"):
    print("Loading ResNetDepth weights...")
    nn.load_parameters("Resnet_Depth_NNabla_model.h5")

landmarks = []
for i, d in enumerate(detected_faces):
    center = [d[2] - (d[2] - d[0]) / 2.0, d[3] - (d[3] - d[1]) / 2.0]
    center[1] = center[1] - (d[3] - d[1]) * 0.12
    scale = (d[2] - d[0] + d[3] - d[1]) / 195
    inp = crop(image, center, scale)
    inp = nn.Variable.from_numpy_array(inp.transpose((2, 0, 1)))
    inp = F.reshape(F.mul_scalar(inp, 1 / 255.0), (1,) + inp.shape)
    with nn.parameter_scope("FAN"):
        out = fan(inp, 4)[-1]
    pts, pts_img = get_preds_fromhm(out, center, scale)
    pts, pts_img = F.reshape(pts, (68, 2)) * \
        4, F.reshape(pts_img, (68, 2))

    heatmaps = np.zeros((68, 256, 256), dtype=np.float32)
    for i in range(68):
        if pts.d[i, 0] > 0:
            heatmaps[i] = draw_gaussian(
                heatmaps[i], pts.d[i], 2)
    heatmaps = nn.Variable.from_numpy_array(heatmaps)
    heatmaps = F.reshape(heatmaps, (1,) + heatmaps.shape)
    with nn.parameter_scope("ResNetDepth"):
        depth_pred = F.reshape(resnet_depth(
            F.concatenate(inp, heatmaps, axis=1)), (68, 1))
    pts_img = F.concatenate(
        pts_img, depth_pred * (1.0 / (256.0 / (200.0 * scale))), axis=1)




pred_type = collections.namedtuple('prediction_type', ['slice', 'color'])
pred_types = {'face': pred_type(slice(0, 17), (0.682, 0.780, 0.909, 0.5)),
              'eyebrow1': pred_type(slice(17, 22), (1.0, 0.498, 0.055, 0.4)),
              'eyebrow2': pred_type(slice(22, 27), (1.0, 0.498, 0.055, 0.4)),
              'nose': pred_type(slice(27, 31), (0.345, 0.239, 0.443, 0.4)),
              'nostril': pred_type(slice(31, 36), (0.345, 0.239, 0.443, 0.4)),
              'eye1': pred_type(slice(36, 42), (0.596, 0.875, 0.541, 0.3)),
              'eye2': pred_type(slice(42, 48), (0.596, 0.875, 0.541, 0.3)),
              'lips': pred_type(slice(48, 60), (0.596, 0.875, 0.541, 0.3)),
              'teeth': pred_type(slice(60, 68), (0.596, 0.875, 0.541, 0.4))
              }