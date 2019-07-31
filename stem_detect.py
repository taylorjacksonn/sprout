import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import random

def get_stem(img, pl):
    rand_gen = random.Random()

    # Make a mask that sets any pixel that is not in a certain 
    # range of green's values to 0 
    hsv = cv2.cvtColor(pl, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (40, 40,40), (70, 255,255)) 
    out_im = cv2.bitwise_and(hsv, hsv, mask=mask)
    out_im = cv2.cvtColor(out_im, cv2.COLOR_HSV2BGR)
    
    extremes = get_extremes(out_im)
   
    return [extremes, out_im]
    

def get_center(img):
    indices = np.where(img != [0])
    x_avg = sum(indices[0]) / (img.shape[0] * img.shape[1])
    y_avg = sum(indices[1]) / (img.shape[0] * img.shape[1])
    return (x_avg, y_avg)


def get_extremes(img):
    indices = np.where(img != [0])
    x_min = min(indices[0])
    x_max = max(indices[0])
    y_min = min(indices[1])
    y_max = max(indices[1])
    return [x_min,x_max,y_min,y_max]

def add_rotation(img):
    rg = random.Random()
    angle = rg.uniform(-1, 1)
    angle = angle * 45
    img = img.rotate(angle, center=(img.size[0]/2, img.size[1]))
    return img

def check_close(corners, x_thresh, y_thresh):
    approved = []
    a,b = corners[0].ravel()
    for point in corners:
        x,y = point.ravel()
        x_dist = x 
        y_dist = y 
        
        if (x_dist > x_thresh[0] and x_dist < x_thresh[1] 
            and y_dist > y_thresh[0] and y_dist < y_thresh[1]): 
            approved.append(point)
    return approved

