import cv2
from matplotlib import pyplot as plt
from PIL import Image
import sys
import numpy as np
import random
import stem_detect

def move_im_to_point(im, point, og_size, fl_size=.05):
    x, y = point
    x_size = og_size[0]
    y_size = og_size[1]
    x_ratio = x / x_size
    y_ratio = y / y_size

    
    new_im = Image.new("RGBA", og_size)

    

    x_size_factor = og_size[0] * fl_size
    y_size_factor = og_size[1] * fl_size

    x_est = og_size[0] * x_ratio
    y_est = og_size[1] * y_ratio 
    region = [(x_est-x_size_factor*.5), y_est-.3*y_size_factor, 
                    (x_est+x_size_factor*.5), y_est+.5*y_size_factor]
    region = [int(el) for el in region]
    reg_size = (region[2] - region[0], region[3] - region[1])
    im = im.resize(reg_size, Image.ANTIALIAS)
        
    new_im.paste(im, box=region)
    return new_im

def check_mask(points, mask):
    approved = []
    for point in points:
        x,y = point.ravel()
        if not (mask[y,x] == [0,0,0]).all():
            approved.append(point)
    return(approved)

def check_overlap(points, im_size, max_flow_size, clumps=False):
    approved = []
    for point in points:
        clear = True
        point_x, point_y = point.ravel()
        for i in approved:
            x,y = i.ravel()
            x_ratio = x / im_size[0]
            y_ratio = y / im_size[1]
            x_est = im_size[0] * x_ratio
            y_est = im_size[1] * y_ratio 
            x_size_factor = im_size[0] * max_flow_size
            y_size_factor = im_size[1] * max_flow_size
            region = [(x_est-x_size_factor*.5), y_est-.3*y_size_factor, 
                    (x_est+x_size_factor*.5), y_est+.5*y_size_factor]
            if (point_x > region[0] and point_x < region[2] and 
                point_y > region[1] and point_y < region[3]):
                if not clumps:
                    clear = False
                    break
            else:
                if clumps:
                    clear = False
                    break
        if clear:
            approved.append(point)
    return approved

def get_placements(img, num):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 10000, 0.01, 5)
    corners = np.int0(corners)
    return corners

def main():
    rand_gen = random.Random()
    fl = cv2.imread(sys.argv[1])
    pl = cv2.imread(sys.argv[2])
    extremes, mask_im  = stem_detect.get_stem(fl, pl) #TODO
    fl[np.where((fl == [0,0,0]).all(axis=2))] = [255,255,255]
    corners = get_placements(pl, 10000)

    clumps = False
    if len(sys.argv) >= 5:
        clumps = bool(int(sys.argv[4]))
    if len(sys.argv) == 7:
        flower_size = (float(sys.argv[5]), float(sys.argv[6]))
    else:
        flower_size = (.07, .15)
    
    fl = cv2.cvtColor(fl.astype(np.uint8), cv2.COLOR_BGRA2RGBA)
    fl = Image.fromarray(fl)
    pl = cv2.cvtColor(pl, cv2.COLOR_BGR2RGB)
    pl = Image.fromarray(pl)
    
    corners = stem_detect.check_close(corners, (extremes[0],
            extremes[1]), (extremes[2], extremes[3])) 
    corners = check_mask(corners, mask_im)
    corners = check_overlap(corners, pl.size, flower_size[1],
                    clumps=clumps)

    pl = pl.convert('RGBA')
    datas = fl.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    fl.putdata(newData)
    
    final_im = Image.new('RGBA', pl.size, (0,0,0,0))
    
    in_size = int(sys.argv[3])
    sample_size = [in_size,len(corners)][bool(len(corners) < in_size)]
    for point in random.sample(corners, sample_size):
        size = rand_gen.uniform(flower_size[0], flower_size[1]) 
        im_point = move_im_to_point(fl, point.ravel(), 
                        pl.size, fl_size=size) 
    
        pl = Image.alpha_composite(pl, im_point)
    
    plt.imshow(pl, zorder=2)
    pl.show()


if __name__ == '__main__':
    main()



