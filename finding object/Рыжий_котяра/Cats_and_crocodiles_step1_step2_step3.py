import numpy as np
import cv2

# Чтение изображеий
image = cv2.imread('catt.jpg')
# Переведём изобрадение в другую цветовую модель/схему
# HSV (англ. Hue, Saturation, Value — тон, насыщенность, значение) 
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# оставим только тон 
hue = hsv_image[:, :, 0] # Канал, который хранит в себе значения тона

# Словарь содержащий в себе диаппазон тонов, относящихся к тому или иному цвету
color_dict_HSV = {'red1': [180, 159],
                  'red2': [9, 0],
                  'green': [89,36],
                  'blue': [128, 90],
                  'yellow': [35, 25],
                  'purple': [158, 129],
                  'orange': [24, 10],
                 }

# Найдём оранжевые пиксели
# Оранжевый цвет лежит в диаппазоне от lower_limit до upper_limit
upper_limit, lower_limit = color_dict_HSV['orange']

# Создадим "маску", элементы которой равны True, если цвет пикселя оранжевый
# и False, если цвет пикселя не оранжевый.
upper = hue < upper_limit # Если значение меньше максимального порога
lower = hue > lower_limit # Если значение больше минимального порога
color_mask = upper & lower # True/False маска удовлетворяющая обоим условиям

# Создадим черный фон (состоит из 0)
background = np.zeros_like(hue)
# Поменяем значения 0 на 255, в тех местах, где на исходном изображении был оранжевый цвет
background[color_mask] = 255

# Отображение изображения на этапе Step1
cv2.imshow("Step1", background)
cv2.imwrite("Step1.jpg", background)
cv2.waitKey(0)

# Применим "findContours" к background
contours, _ = cv2.findContours(background, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Нарисуем контуры на изображении
image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 3)

# Отображение изображения с контурами на этапе Step2
cv2.imshow("Step2", image_with_contours)
cv2.imwrite("Step2.jpg", image_with_contours)
cv2.waitKey(0)

# Оставим контур с самой большой площадью
ind = 0
area_max = 0
for n, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if area > area_max:
        area_max = area
        ind = n

# Найдём ограничивающую рамку самого большого контура
cnt = contours[ind]
x, y, w, h = cv2.boundingRect(cnt)

# Нарисуем рамку на исходном изображении
image = cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)


# Отображение изображения на этапе Step2
cv2.imshow("Step3", image)
cv2.imwrite("Step3.jpg", image)
cv2.waitKey(0)
