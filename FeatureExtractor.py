'''
Extract features from images
'''
import cv2
import numpy as np
from os import listdir
from scipy.io import savemat

# get image name list
image_names = [im for im in listdir('./data/Flicker8k_Dataset')]
print 'number of images', len(image_names)

# create feature extractor
surf = cv2.xfeatures2d.SURF_create()
# create features data
feats = {'feats': [],
         '__globals__': [],
         '__header__': b'MATLAB 5.0 MAT-file Platform: Ubuntu, Zhenguo Chen',
         '__version__': '1.0'}

# extract features from images
for im_name in image_names[:10]:
    img = cv2.imread('./data/Flicker8k_Dataset/'+im_name)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # find the keypoints and descriptors with SIFT
    kp, des = surf.detectAndCompute(img,None)
    # set descriptor to the same size
    flat = des.flatten()
    flat.resize(8000)

    # feats['feats'] = np.append(feats['feats'], flat)
    feats['feats'].append(flat.tolist())

savemat('./data/Flicker8k_KNN/knn_feats.mat', feats)

