# краткая докуменнтация
# https://pythonpip.ru/opencv/kontury
import cv2

# Открываем изображение
image = cv2.imread('test_rectangle.jpg')

# Преобразуем изображение в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Test color', gray)
cv2.waitKey(0)

# Вызовем функцию  Canny к оттенкам серого изображения gray с нижним порогом 30 и верхним порогом 200, чтобы найти границы на изображении.
gray = cv2.Canny(gray, 30, 200)
# Находим контуры на изображении
contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



# Рисуем контуры на изображении
image_with_contours = image.copy()
cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 3)

# Добавляем текст "Это был Красный квадрат" в левом верхнем углу
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image_with_contours, "Это был Красный квадрат", (50, 50), font, 1, (255, 0, 0), 2)

# Сохраняем изображение с контурами и текстом
cv2.imwrite('test_rectangle_find.jpg', image_with_contours)

# Отображаем изображение с контурами и текстом
cv2.imshow('Contours', image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
