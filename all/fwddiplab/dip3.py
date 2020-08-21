import cv2

img1 = cv2.imread('../Desktop/labimg.jpg')
img2 = cv2.imread('../Desktop/flower.jpg')
res = cv2.resize(img2, dsize=(332, 300), interpolation=cv2.INTER_CUBIC)
cv2.imwrite("../Desktop/resized.jpg",res)
dst = cv2.addWeighted(img1,0.5,res,0.5,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
