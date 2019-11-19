import cv2 as cv
import numpy as np

src = cv.imread("AK.Jpeg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)

# numpy克隆图像
m1 = np.copy(src)

m2 = src
src[100:200,200:300,:] = 0
cv.imshow("m2",m2)

m3 = np.zeros(src.shape, src.dtype)#创建一个全黑的图片（全0填充），大小与src相同
cv.imshow("m3", m3)

m4 = np.zeros([512,512], np.uint8)#创建一个全黑的图片（全0填充），大小512X512，将图像转化为up.uint8形式
# m4[:,:] =127 try to give gray value 127
cv.imshow("m4", m4)

m5 = np.ones(shape=[512,512,3], dtype=np.uint8)
m5[:,:,0] = 255
cv.imshow("m5", m5)

cv.waitKey(0)
cv.destroyAllWindows()
#good
#good
