
'''
Codes for saving sketch images.
Thanks to higumax (https://github.com/higumax)

[original] : https://github.com/higumax/sketchKeras-pytorch/blob/master/src/test.py

modified by : STomoya (https://github.com/STomoya)

modified the code so that the generating sketch flow can be called from external files.
'''

import argparse
import numpy as np
import torch
import cv2
from .model import SketchKeras

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SketchKeras().to(device)
model.load_state_dict(torch.load('/usr/src/sketchKeras/weights/model.pth'))

def preprocess(img):
    h, w, c = img.shape
    blurred = cv2.GaussianBlur(img, (0, 0), 3)
    highpass = img.astype(int) - blurred.astype(int)
    highpass = highpass.astype(np.float) / 128.0
    highpass /= np.max(highpass)

    ret = np.zeros((512, 512, 3), dtype=np.float)
    ret[0:h,0:w,0:c] = highpass
    return ret


def postprocess(pred, thresh=0.18, smooth=False):
    assert thresh <= 1.0 and thresh >= 0.0

    pred = np.amax(pred, 0)
    pred[pred < thresh] = 0
    pred = 1 - pred
    pred *= 255
    pred = np.clip(pred, 0, 255).astype(np.uint8)
    if smooth:
        pred = cv2.medianBlur(pred, 3)
    return pred

def resize(img):
    height, width = float(img.shape[0]), float(img.shape[1])
    if width > height:
        new_width, new_height = (512, int(512 / width * height))
    else:
        new_width, new_height = (int(512 / height * width), 512)
    img = cv2.resize(img, (new_width, new_height))
    return img, new_width, new_height

def gen_sketchkeras_image(src, dst):
    img = cv2.imread(src)
    img, new_width, new_height = resize(img)

    img = preprocess(img)
    x = img.reshape(1, *img.shape).transpose(3, 0, 1, 2)
    x = torch.tensor(x).float()

    with torch.no_grad():
        pred = model(x.to(device))
    pred = pred.squeeze()

    output = pred.cpu().detach().numpy()
    output = postprocess(output, thresh=0.1, smooth=False) 
    output = output[:new_height, :new_width]

    cv2.imwrite(dst, output)

if __name__ == "__main__":
    gen_sketchkeras_image('sample.jpg', 'sketchkeras.jpg')


    