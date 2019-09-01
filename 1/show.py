from encoder import XML2Dict
import cv2
import os
import glob
import numpy
path=os.path.dirname(os.path.realpath(__file__))+r'\*.bmp'
mkdirpath=os.path.dirname(os.path.realpath(__file__))+'\\result\\'
folder = os.path.exists(mkdirpath)
if not folder:
    os.makedirs(mkdirpath)
for filename in glob.glob(path):
    xml = XML2Dict()
    xmlpath=filename.replace('bmp', 'xml')
    with open(xmlpath, 'r', encoding='utf-8') as f:
        s = f.read()           
        the_dict = xml.parse(s) 
        #print(the_dict)
    img=pirate=cv2.imread(filename)
    annotation = the_dict['annotation']
    _object = annotation['object']
    flag=False  
    for obj in _object:
        if obj=='name':
            flag=True
            break
        name = obj['name'].decode('utf-8')
        bndbox = obj['bndbox']   
        xmin = int(bndbox['xmin'])
        ymin = int(bndbox['ymin'])
        xamx = int(bndbox['xmax'])
        ymax = int(bndbox['ymax'])
        img=cv2.rectangle(img, (xmin, ymin), (xamx, ymax), (0, 255, 0), 2)
        cv2.putText(img, str(name), (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
    if flag:
        name = _object['name'].decode('utf-8')
        bndbox = _object['bndbox']   
        xmin = int(bndbox['xmin'])
        ymin = int(bndbox['ymin'])
        xamx = int(bndbox['xmax'])
        ymax = int(bndbox['ymax'])  
        cv2.putText(img, str(name), (xmin, ymin-2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        img=cv2.rectangle(img, (xmin, ymin), (xamx, ymax), (0, 255, 0), 2)
    filepahe=os.path.dirname(os.path.realpath(__file__))+r'\\result\\'+os.path.basename(filename)
    cv2.imwrite(filepahe, img)
    print('save '+filepahe)

