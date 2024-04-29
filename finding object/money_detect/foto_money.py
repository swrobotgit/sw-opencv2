import cv2

# Загрузка изображения
img = cv2.imread('1rubl.jpg')
#img = cv2.imread('circle_test.jpg') можно попробывать такое изображение

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
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=300,
                               param1=150, param2=30, minRadius=100, maxRadius=200)



if circles is not None:
    circles = circles[0]

    for circle in circles:
        center = (int(circle[0]), int(circle[1]))  # Преобразуем координаты центра в целые числа
        radius = int(circle[2])  # Преобразуем радиус в целое число
        cv2.circle(img, center, radius, (0, 255, 0), 2)

# Отображаем изображение с найденными кругами
cv2.imshow('Circle Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
