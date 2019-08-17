from encoder import XML2Dict
import glob
import os
classes = ['pockmark','corrosion','crack','rebar']
path=os.path.dirname(os.path.realpath(__file__))+r'\*.xml'
trainpath=os.path.dirname(os.path.realpath(__file__))+r'\train.txt'
for filename in glob.glob(path):
    xml = XML2Dict()
    with open(filename, 'r', encoding='utf-8') as f:
        s = f.read()           
        the_dict = xml.parse(s) 
    annotation = the_dict['annotation']
    _object = annotation['object']
    flag=False
    info = filename.replace('xml', 'bmp')
    for obj in _object:
        if obj=='name':
            flag=True
            break
        name = obj['name'].decode('utf-8')
        bndbox = obj['bndbox']   
        xmin = int(bndbox['xmin'])
        ymin = int(bndbox['ymin'])
        xmax = int(bndbox['xmax'])
        ymax = int(bndbox['ymax'])        
        info +=' '+str(xmin)+','+str(ymin)+','+str(xmax)+','+str(xmax)+','+str(classes.index(name))
    if flag:
        name = _object['name'].decode('utf-8')
        bndbox = _object['bndbox']   
        xmin = int(bndbox['xmin'])
        ymin = int(bndbox['ymin'])
        xmax = int(bndbox['xmax'])
        ymax = int(bndbox['ymax'])  
        info +=' '+str(xmin)+','+str(ymin)+','+str(xmax)+','+str(xmax)+','+str(classes.index(name))
    print(info)
    with open(trainpath, 'a') as f:
        f.write(info + "\n")
