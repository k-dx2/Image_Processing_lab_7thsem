import cv2
import numpy as np
from matplotlib import pyplot as plt

im = cv2.imread('pil.jpg')
for i in range(0, len(im)):
  for j in range(0, len(im[0])):
    print(im[i][j])
  print("\n")
cv2.imshow('image',im)
cv2.imwrite("out.png", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
