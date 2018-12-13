import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import random

def get_stem(img, pl):
    #pl = cv2.imread('potted.jpg')
    rand_gen = random.Random()
    hsv = cv2.cvtColor(pl, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (40, 40,40), (70, 255,255)) 
    out_im = cv2.bitwise_and(hsv, hsv, mask=mask)
    out_im = cv2.cvtColor(out_im, cv2.COLOR_HSV2BGR)
    
    extremes = get_extremes(out_im)
    
    color_arr = []
    while(len(color_arr) < 20):
        hei, wid, chan = pl.shape

        x = rand_gen.randint(0, wid-1)
        y = rand_gen.randint(0, hei-1)
    
        col = out_im[y, x].astype(np.uint8)
        if not (col == [0,0,0]).all():
            color_arr.append(col)

    height, width, channels = img.shape
    top_left = (int(width * .48), int(height *.45))
    bottom_right = (int(width * .52), int(height))
    new_im = np.zeros((height, width, 3))
    new_im[:,:] = [255,255,255]
    new_im = cv2.rectangle(new_im,top_left, bottom_right,(0,255,0),
                    thickness=cv2.FILLED) # 3)

    for i in range(top_left[0], bottom_right[0]):
        for j in range(top_left[1], bottom_right[1]):
            new_im[j, i] = color_arr[rand_gen.randint(0, 19)]

    #new_im[np.where((img != [0,0,0]).all(axis=2))] = img[
    #                np.where((img != [0,0,0]).all(axis=2))]
    #new_im[np.where((new_im == [0,0,0]).all(axis=2))] = [255,255,255] 
    return [out_im, extremes, out_im]#get_center(img)]
    

def get_center(img):
    indices = np.where(img != [0])
    #coordinates = zip(indices[0], indices[1])
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
    """
    M = cv2.getRotationMatrix2D((img.shape[0]/2, img.shape[1]), 
            angle, 1)
    img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    """
    img = img.rotate(angle, center=(img.size[0]/2, img.size[1]))
    return img






def check_close(corners, x_thresh, y_thresh):
    approved = []
    a,b = corners[0].ravel()
    for point in corners:
        x,y = point.ravel()
        """
        dist = (x - center[0]) ** 2
        dist += (y-center[1]) ** 2
        dist = dist ** .5
        """
        
        #dist = ((x - center[0])**2 + 
        #                (y-center[1]**2))**.5 
        #print("DIST ")
        #print(dist)
        
        
        
        #if dist < thresh:
         
        x_dist = x #abs(x - center[0])  
        y_dist = y #abs(y - center[1])
        
        
        if (x_dist > x_thresh[0] and x_dist < x_thresh[1] 
            and y_dist > y_thresh[0] and y_dist < y_thresh[1]): 
            approved.append(point)
    return approved

