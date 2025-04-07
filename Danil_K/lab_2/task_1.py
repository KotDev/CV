import cv2

def get_hsv_image(file_name: str): # Пишем функцию перевода изображения в hsv формат, на входе нужно передать имя файла
    img = cv2.imread(f"images/{file_name}", flags=1) # считываем изображение
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # переводим изображение в hsv
    # Возвращаем исходное изображение и hsv изображение
    return hsv_img, img

