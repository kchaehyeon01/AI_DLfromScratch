#%%
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("honeybadger.jpeg")
plt.imshow(img)
plt.show()