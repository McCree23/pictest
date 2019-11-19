import  os
import  cv2
import numpy
pwd=os.getcwd()
name=os.listdir(pwd)
for filename in name:
    if(filename[-4:]=='Jpeg'):
        img=cv2.imread(pwd+'\\'+filename)
        avg=numpy.mean(img)
        if(avg<50):
            os.remove(filename)
            print('移除'+filename)
