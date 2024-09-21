import pyautogui
from PIL import ImageGrab
import keyboard
import time

# Задержка между проверками (в секундах)
delay = 0.1

# Переменные для хранения цвета пикселя и его координат
target_color = None
x, y = None, None

# Флаг, указывающий на то, что мы выбираем целевой цвет
choosing_color = False

# Функция для обработки нажатия клавиши
def on_key_press(event):
    global choosing_color
    if event.name == "alt":  # Нажмите Alt для начала выбора целевого цвета
        choosing_color = True

# Регистрируем функцию обработки нажатия клавиши
keyboard.on_press(on_key_press)

try:
    while True:
        if choosing_color:
            print("Выберите целевой цвет, наведя курсор на соответствующий пиксель и нажав Alt...")
            # Получаем координаты курсора и цвет пикселя под ним
            x, y = map(int, pyautogui.position())
            screenshot = ImageGrab.grab()
            target_color = screenshot.getpixel((x, y))
            print("Выбранный цвет:", target_color)
            choosing_color = False  # Заканчиваем выбор цвета
        else:
            # Снимаем скриншот экрана и получаем цвет пикселя
            screenshot = ImageGrab.grab()
            pixel_color = screenshot.getpixel((x, y))
            
            # Если цвет пикселя изменился на целевой цвет, эмулируем нажатие левой кнопки мыши
            if pixel_color == target_color:
                pyautogui.click()
                print("Пиксель изменил цвет. Произведено нажатие левой кнопки мыши.")
            
            # Подождать некоторое время перед следующей проверкой
            time.sleep(delay)
except KeyboardInterrupt:
    # Если пользователь нажмет Ctrl+C, программа завершит работу
    print("Программа завершена")