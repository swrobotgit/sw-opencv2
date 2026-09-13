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

# Подсчитываем количество контуров
num_contours = len(contours)
# print(contours)
# Выводим количество контуров в консоль
print("Найдено контуров: "+ str(num_contours))

# Перебираем все контуры
for contour in contours:
    # Получаем координаты контура
    for point in contour:
        x, y = point[0]
        # Выводим координаты в консоль
        print(f"Координаты точки: x={x}, y={y}")

# Инициализируем переменные для хранения крайних координат
top_left = None
bottom_right = None

# Перебираем все контуры
for contour in contours:
    for point in contour:
        x, y = point[0]
        # Находим крайние координаты
        if top_left is None or (x <= top_left[0] and y <= top_left[1]):
            top_left = (x, y)
        if bottom_right is None or (x >= bottom_right[0] and y >= bottom_right[1]):
            bottom_right = (x, y)

# Выводим крайние координаты
print("Крайняя верхняя левая координата:", top_left)
print("Крайняя нижняя правая координата:", bottom_right)


# Рисуем контуры на изображении
image_with_contours = image.copy()

# Рисуем прямоугольник на изображении
cv2.rectangle(image_with_contours, top_left, bottom_right, (0, 0, 0), thickness=2)

# Находим координаты середины прямоугольника
center_x = (top_left[0] + bottom_right[0]) // 2
center_y = (top_left[1] + bottom_right[1]) // 2

# Получаем цвет пикселя в середине прямоугольника
pixel_color = image[center_y, center_x]

# Выводим значение RGB цвета пикселя
print("RGB значение цвета пикселя в середине прямоугольника:"+ str(pixel_color))

# Добавляем текст "Это был Красный квадрат" в левом верхнем углу
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image_with_contours, "Цвет этого прямоугольника: "+str(pixel_color), (50, 50), font, 1, (255, 0, 0), 1)

# Сохраняем изображение с контурами и текстом
cv2.imwrite('test_rectangle_find.jpg', image_with_contours)

# Отображаем изображение с контурами и текстом
cv2.imshow('Contours', image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
