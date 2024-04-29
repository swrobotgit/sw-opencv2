import cv2
import mediapipe as mp


# Функция для проверки положения руки: выше ли точка кисти руки точки плеча
# Не забываем, что координаты у нас плавующие ! и все сравнения происходит в динамики
def check_hand_up(landmarks):
    # Получаем координаты левого плеча и кисти руки из landmarks
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]

    # Проверяем, если координата y кисти руки меньше координаты y плеча
    if left_wrist.y < left_shoulder.y:
        return True  # Возвращаем True, если рука поднята
    else:
        return False  # Возвращаем False, если рука опущена



# Инициализация рисования результатов и работы с позой
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Захват видеопотока с камеры
cap = cv2.VideoCapture(0)

# Создание экземпляра класса Pose с параметрами confidence
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Преобразование BGR в RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Обработка кадра для обнаружения позы
        results = pose.process(image)

        # Проверка наличия обнаруженной позы
        if results.pose_landmarks:
            # Отрисовка ключевых точек позы
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            # Добавление номеров точек на изображение
            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                h, w, _ = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.putText(frame, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Проверка положения руки и вывод подписи
            if check_hand_up(results.pose_landmarks.landmark):
                cv2.putText(frame, 'Рука поднята', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        # Отображение кадра с позой
        cv2.imshow('Pose Detection', frame)

        # Выход из цикла при нажатии клавиши q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Освобождение ресурсов и закрытие окон OpenCV
cap.release()
cv2.destroyAllWindows()
