import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg',0)
edges = cv2.Canny(img,100,200)
cv2.imshow("image1", edges)
cv2.waitKey(0)

def convolve(image, kernel):
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * kernel).sum()
			output[y - pad, x - pad] = k
	return output

point_dect = np.array((
	[-1, -1, -1],
	[-1,  3, -1],
	[-1, -1, -1]), dtype="int")

convoleOutput = convolve(edges, point_dect)
cv2.imshow("image2", convoleOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()

