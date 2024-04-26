import numpy as np
import cv2

# Чтение изображеий
image = cv2.imread('obj_2.png')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.imread('obj_2.png', 0)

# Перед тем как найти контур, необходимо перевести цветное изображение к чернобелому
# set a thresh
thresh = 150
# px =  0  if px < thresh
# px = 255 if px > thresh
# get threshold image
ret, thresh_img = cv2.threshold(image_gray, thresh, 255, cv2.THRESH_BINARY)

# Применим "findContours" к чернобелому изображению
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Оставим только контуры с большой площадью
img_contours = np.uint8(np.zeros((image.shape[0], image.shape[1])))
tr_contours = []
for countour in contours[1:]:
    area = cv2.contourArea(countour)
    if area > 10000:
        tr_contours.append(countour)

# Нанесём найденные контуры на RGB-изображение
# cv2.drawContours(image, tr_contours, -1, (155,0,155), 2)
cv2.drawContours(image=image, contours=tr_contours,
                 contourIdx=-1, color=(155, 0, 155),
                 thickness=3, lineType=cv2.LINE_AA)
tr_contours = np.array(tr_contours)

# Найдём центр каждого контура
centers = []
for countour in tr_contours:
    centers.append(countour.mean(axis=0)[0])
centers = np.array(centers)

# Определим цвета фигур (значение цвета в центральном пикселе)
colors = []
for x, y in centers:
    colors.append(image[int(y), int(x)])
colors = np.array(colors)

# найдем уникальные цвета:
# values - значение цвета; counts - количество
values, counts = np.unique(colors, axis=0, return_counts=True)

# Превращаем np.array в кортеж (tuple), чтобы использовать в качестве ключей словаря
colors_typle = [tuple(el) for el in values]

# создаем словарь со значениями цветов
colors_map = {(0, 128, 0): 'green', (0, 255, 0): 'green', (255, 0, 0): 'blue',
              (0, 0, 255): 'red', (255, 255, 255): 'white', (0, 0, 0): 'black'}

# Запишем результат в отдельный список (цвет : количество квадратов)
results = []
results.append(f'Всего найдено : {counts.sum()}')
for n, color in enumerate(colors_typle):
    s = f'{colors_map.get(color)} : {counts[n]}'
    results.append(s)

# Добавим получившийся результат на изображение:

# Сперва зададим параметры шрифта
font = cv2.FONT_HERSHEY_COMPLEX  # Шрифт
fontScale = 1  # масштаб шрифта
fontColor = (0, 0, 0)  # цвет шрифта
thickness = 2  # толщина
lineType = 2  # тип линии

# напишем название цвета в центр каждого квадрата
for x, y in centers:
    color = image[int(y), int(x)]
    color = colors_map.get(tuple(color))
    if color == 'white':
        continue
    cv2.putText(image, color,
                (int(x) - 40, int(y) - 10),
                font, fontScale,
                fontColor, thickness, lineType)

# Чтобы записать результат в белый прямоугольник
# Найдём координаты белого прямоугольника
white = np.where((values[:, 0] == 255) & (values[:, 1] == 255) & (values[:, 2] == 255))
white_coord = tr_contours[white]
white_coord = tuple(white_coord[0][0])[0]
white_coord = white_coord[0] + 20, white_coord[1] + 150

bottomLeftCornerOfText = tuple(white_coord)  # (x, y)
thickness = 1

for res in results:
    cv2.putText(image, res,
                bottomLeftCornerOfText,
                font, fontScale,
                fontColor, thickness, lineType)
    # каждая новая строка ниже предыдущей на 30 px
    bottomLeftCornerOfText = bottomLeftCornerOfText[0], bottomLeftCornerOfText[1] + 30

# Display the image
cv2.imshow("img", image)
# Save image
cv2.imwrite("out.jpg", image)
cv2.waitKey(0)
