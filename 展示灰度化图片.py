import  os
import  cv2
import numpy
pwd=os.getcwd()
name=os.listdir(pwd)
for filename in name:
    if(filename[-4:]=='Jpeg'):
        img=cv2.imread(pwd+'\\'+filename)#读取一个图片，定义名称为img
        cv2.namedWindow('input', cv2.WINDOW_AUTOSIZE)#定义显示窗口尺寸
        cv2.imshow('input', img)#展示图片img，窗口名为input
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#将img转化为cv2.COLOR_BGR2GRAY类型，定义名称为gray
        cv2.imwrite('gray.png', gray)#把gary输出为图片，定义名称为gray.png
        cv2.imshow('gray', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

