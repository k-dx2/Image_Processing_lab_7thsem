import cv2

img = cv2.imread("1.jpg")
print(img.shape)
dsize = (100, 100)
img = cv2.resize(img, dsize)
print(img.shape)
