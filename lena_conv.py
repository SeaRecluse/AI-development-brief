import cv2
import numpy as np
import time

def convolution(imgList,covMatrix,h,w):
	covImg = []

	for i in range(h):
		perCov = []
		for j in range(w):
			res = [[covMatrix[0][0] * imgList[i][j] + covMatrix[0][1] * imgList[i + 1][j],\
					covMatrix[0][0] * imgList[i][j + 1] + covMatrix[0][1] * imgList[i + 1][j + 1]],\
					[covMatrix[1][0] * imgList[i][j] + covMatrix[1][1] * imgList[i + 1][j],\
					covMatrix[1][0] * imgList[i][j + 1] + covMatrix[1][1] * imgList[i + 1][j + 1]]]

			resValue = abs(res[0][0]*res[1][1] - res[0][1]*res[1][0])%255
			perCov.append(resValue)
		covImg.append(perCov)

	return covImg

lena = cv2.imread("lena.bmp")
h = len(lena)
w = len(lena[0])
grey_list = []
for i in range(h):
	per_grey = []
	for j in range(w):
		r = lena[i,j][2]
		g = lena[i,j][1]
		b = lena[i,j][0]
		grey =  int(0.3 * r + 0.59 * g + 0.11 * b)
		lena[i,j][0] = grey
		lena[i,j][1] = grey
		lena[i,j][2] = grey
		per_grey.append(grey)
	per_grey.append(0)
	grey_list.append(per_grey)
per_grey = []
for i in range(w + 1):
	per_grey.append(0)
grey_list.append(per_grey)

cv2.imshow("lena",lena)

cv2.waitKey(1)
convolutionMatrix = [[0.1,0.5],[0,0.5]]
lenaChangeList = convolution(grey_list,convolutionMatrix,h,w)

for i in range(h):
	for j in range(w):
		lena[i,j][0] = lenaChangeList[i][j]
		lena[i,j][1] = lenaChangeList[i][j]
		lena[i,j][2] = lenaChangeList[i][j]


cv2.imshow("lenaC",lena)
cv2.waitKey(50000)