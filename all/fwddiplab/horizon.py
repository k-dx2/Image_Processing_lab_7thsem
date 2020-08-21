#rom skimage.exposure import rescale_intensity
import numpy as np
import cv2

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
	[2,  2, 2],
	[-1, -1, -1]), dtype="int")

image = cv2.imread("house.jpg", 0)
gray = image
cv2.imshow("image", image)
cv2.waitKey(0)

convoleOutput = convolve(gray, point_dect)
cv2.imshow("image", convoleOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()

