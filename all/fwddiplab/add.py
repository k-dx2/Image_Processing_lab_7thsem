import cv2 
  
# Read Image1 

cat = cv2.imread('1.jpg') 
  
# Read image2 
sky = cv2.imread('pil.jpg') 
dsize = (cat.shape[1], cat.shape[0])
sky = cv2.resize(sky, dsize)
# Add the images 
img = cv2.add(cat, sky) 
  
# Show the image 
cv2.imshow('image', img)
  
# Wait for a key 
cv2.waitKey(0) 
  
# Destroy all the window open 
cv2.destroyAllWindows() 
