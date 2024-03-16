import pyautogui
import keyboard
import time

def get_click_position(prompt):
    print(prompt)
    keyboard.wait('s')
    return pyautogui.position()

print("Переместите курсор на первую позицию и нажмите 's'.")
pos1 = get_click_position("Первая позиция захвачена. Переместите курсор на вторую позицию и нажмите 's' для захвата.")

pos2 = get_click_position("Вторая позиция захвачена. Нажмите 's' для начала цикла кликов.")

# Интервалы для каждой позиции
interval1 = 3  # Интервал для первой позиции
interval2 = 4  # Интервал для второй позиции

print(f"Клики начнутся в позициях {pos1} и {pos2}. Нажмите 'q' для остановки.")

last_click_time1 = time.time() - interval1  # Инициализация времени для первой позиции
last_click_time2 = time.time() - interval2  # Инициализация времени для второй позиции

try:
    while True:
        current_time = time.time()
        if current_time - last_click_time1 >= interval1:
            pyautogui.click(pos1)
            last_click_time1 = current_time
        if current_time - last_click_time2 >= interval2:
            pyautogui.click(pos2)
            last_click_time2 = current_time

        if keyboard.is_pressed('q'):
            print("Автокликер остановлен.")
            break
except KeyboardInterrupt:
    print("Автокликер остановлен.")
