import numpy as np
import cv2

# Чтение изображеий
image = cv2.imread('obj_2.png')
hsvimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# upper_limit & lower_limit
# Нам нужен только тон - Hue
color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}

# Найдём синие пиксели
upper_limit = 128
lower_limit = 90

for i in range(hsvimage.shape[0]):
    line = hsvimage[i,::,::]
    upper = line[::,0]<upper_limit # Если значение меньше максимального порога
    lower = line[::,0]>lower_limit # Если значение больше минимального порога
    color_mask = upper & lower #  True/False маска удовлетворяющая обоим условиям
    if len(color_mask[color_mask==True]) >= 1: # Хотябы один пиксель синий
        ind, = np.where(color_mask == True)
        min_ind = ind.min()
        max_ind = ind.max()