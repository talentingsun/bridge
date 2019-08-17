from encoder import XML2Dict
import cv2
import glob
import os
path=os.path.dirname(os.path.realpath(__file__))+r'\*.bmp'
a=glob.glob(path)
aaaa=a.__len__()
for filename in glob.glob(path):
    imgpath=filename.replace('bmp', 'xml')
    print(filename)
    print(imgpath)