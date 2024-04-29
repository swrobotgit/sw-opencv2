# В данной коде используются 3 метода поиска круглых объектов : HoughCircles, findContours, Canny - оцените результаты их работы и сделайте выводы.
import cv2
import numpy as np

# Загрузка изображения
img = cv2.imread('circle_test.jpg')

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Поиск кругов
# cv2.HoughCircles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
# dp - Разрешение обратного преобразования Хафа (dp=1 - размер изображения)
# minDist - Минимальное расстояние между центрами найденных кругов
# param1 - Первый параметр метода детекции кругов (чувствительность детектора)
# param2 - Второй параметр метода детекции кругов (пороговое значение для центров круживает ругов)
# minRadius - Минимальный радиус искомых кругов
# maxRadius - Максимальный радиус искомых кругов
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]
        cv2.circle(img, center, radius, (0, 255, 0), 2)

# Поиск контуров
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

# Поиск границ
edges = cv2.Canny(gray, 100, 200)

# Отображение результатов в окнах
cv2.imshow('HoughCircles', img)
cv2.imshow('findContours', img)
cv2.imshow('Canny', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
