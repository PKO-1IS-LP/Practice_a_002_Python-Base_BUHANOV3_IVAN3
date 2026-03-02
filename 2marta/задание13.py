import tkinter as tk

window = tk.Tk()
window.title("Меню")
window.geometry("280x420")
window.configure(bg="#2F2F2F")

def button_click(text):
    # Функция вызывается при нажатии на кнопку
    # text - текст нажатой кнопки
    print(f"Нажата кнопка: {text}")  # Вывод в консоль

# Создаем контейнер для центрирования всех кнопок
main_frame = tk.Frame(window, bg="#2F2F2F")
main_frame.pack(expand=True)  # expand=True центрирует контейнер

# Список текстов для кнопок
buttons_text = ["Главная", "Профиль", "Друзья", "Сообщения", "Настройки"]

