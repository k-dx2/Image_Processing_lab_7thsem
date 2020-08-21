import matplotlib.pyplot as plt
import matplotlib.image as img

image=img.imread("image.jpg")
plt.imshow(image,cmap="gray")
plt.show()
