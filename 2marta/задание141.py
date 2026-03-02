import tkinter as tk

# Создаем главное окно
window = tk.Tk()
window.title("Профиль")
window.geometry("400x500")
window.configure(bg="#F0F4F8")  # Светло-голубовато-серый фон

# Заголовок профиля (имя)
label_name = tk.Label(
    window,
    text="Буханов Иван",
    font=("Georgia", 32, "bold"),
    fg="#1A3C5A",  # Темно-синий цвет
    bg="#F0F4F8"  # Тот же фон, что и у окна
)
label_name.pack(pady=(30, 0))  # Отступ сверху 30px, снизу 0

# Никнейм (username)
label_username = tk.Label(
    window,
    text="Ivan20",
    font=("Courier", 18),
    fg="#666666",  # Серый цвет
    bg="#F0F4F8"
)
label_username.pack(pady=(5, 20))  # Небольшой отступ сверху, снизу 20px

# Создаем фрейм-контейнер для белого блока
white_frame = tk.Frame(
    window,
    width=300,
    height=180,
    bg="white",  # Белый фон
    bd=2,  # Толщина рамки 2 пикселя
    relief="solid"  # Сплошная рамка (не объемная)
)
white_frame.pack(pady=10)  # Отступы сверху и снизу
white_frame.pack_propagate(False)  # Запрещаем изменение размера под содержимое

# Текст внутри белого фрейма
label_profession = tk.Label(
    white_frame,
    text="Студент коледжа",
    font=("Arial", 20, "bold"),
    fg="#2E8B57",  # Зеленый цвет (морская волна)
    bg="white"  # Белый фон
)
label_profession.pack(expand=True)  # Центрируем внутри фрейма

window.mainloop()