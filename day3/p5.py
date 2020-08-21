import cv2
import numpy as np

img=cv2.imread("image.jpeg",0)

h=img.shape[0]
w=img.shape[1]

for x in range(0,w):
	for y in range(0,h):

