# Полное руководство по tkinter
## (Расширенная версия со стикерами и заметками)

---

## Содержание
1. [Введение в tkinter](#введение-в-tkinter)
2. [Основные виджеты](#основные-виджеты)
3. [Упаковщики (менеджеры геометрии)](#упаковщики-менеджеры-геометрии)
4. [Привязка событий](#привязка-событий)
5. [Продвинутые виджеты](#продвинутые-виджеты)
6. [Методы виджетов](#методы-виджетов)
7. [Диалоговые окна](#диалоговые-окна)
8. [Примеры программ](#примеры-программ)
9. [Стикеры и заметки](#стикеры-и-заметки)

---

## Введение в tkinter

> 📌 **Важно!**  
> Этой библиотеке посвящено мало внимания, и найти в рунете курс, книгу или FAQ по ней довольно-таки сложно.

### Что такое tkinter?

**Tkinter** — это графическая библиотека, позволяющая создавать программы с оконным интерфейсом на Python.

> 💡 **Интересный факт**  
> Библиотека портирована из популярного на UNIX-системах инструментария Tk.

> 🏷️ **Термин**  
> **Виджеты** — стандартизированные компоненты графического пользовательского интерфейса, с которыми взаимодействует пользователь.

### Импорт библиотеки

```python
from tkinter import *
```

> ⚠️ **Внимание!**  
> В Python 2 нужно писать `Tkinter` с большой буквы, в Python 3 — `tkinter` с маленькой.

### Создание главного окна

```python
root = Tk()  # создание главного окна
root.title('Моя программа')  # заголовок окна
root.geometry('400x300')  # размер окна (ширина x высота)
root.mainloop()  # главный цикл обработки событий
```

> 🎯 **Ключевой момент**  
> `mainloop()` запускает бесконечный цикл обработки событий. Без этой команды окно мгновенно закроется!

> 📝 **Заметка**  
> `root` — это общепринятое название для главного окна, но вы можете назвать его как угодно.

---

## Основные виджеты

### Button (Кнопка)

```python
button1 = Button(root, text='ok', width=25, height=5, 
                 bg='black', fg='red', font='arial 14')
button1.pack()
```

> 🔍 **Детали**  
> `width` и `height` задаются в символах, не в пикселях!

> 🎨 **Цвета**  
> - `bg` (background) — цвет фона  
> - `fg` (foreground) — цвет текста

### Label (Метка)

```python
label1 = Label(root, text='Привет!', font='Arial 20', fg='blue')
label1.pack()
```

> ℹ️ **Для информации**  
> `Label` используется только для отображения текста, пользователь не может его редактировать.

### Entry (Поле ввода)

```python
entry1 = Entry(root, width=30, bd=5)  # bd - borderwidth (ширина границы)
entry1.pack()
```

> 📌 **Совет**  
> `bd` (borderwidth) увеличивает границу поля, делая его более заметным.

### Text (Многострочное поле)

```python
text1 = Text(root, height=7, width=7, font='Arial 14', wrap=WORD)
text1.pack()
```

> 🔄 **Режимы переноса**  
> - `WORD` — перенос по словам  
> - `CHAR` — перенос по символам  
> - `NONE` — без переноса

### Listbox (Список)

```python
listbox1 = Listbox(root, height=5, width=15, selectmode=EXTENDED)
```

> ✅ **Режимы выбора**  
> - `SINGLE` — только один пункт  
> - `EXTENDED` — несколько пунктов (с Ctrl/Shift)  
> - `BROWSE` — выбор движением мыши  
> - `MULTIPLE` — несколько пунктов простым кликом

### Frame (Рамка)

```python
frame1 = Frame(root, width=100, height=100, bg='green', bd=5)
```

> 🖼️ **Для чего нужен Frame**  
> Контейнер для группировки виджетов. Помогает лучше организовать интерфейс.

### Checkbutton (Флажок)

```python
var1 = IntVar()  # специальная переменная
check1 = Checkbutton(root, text='1 пункт', variable=var1, onvalue=1, offvalue=0)
```

> 🔢 **Типы переменных tkinter**  
> - `IntVar()` — для целых чисел  
> - `StringVar()` — для строк  
> - `BooleanVar()` — для булевых значений  
> - `DoubleVar()` — для чисел с плавающей точкой

### Radiobutton (Переключатель)

```python
var = IntVar()
rbutton1 = Radiobutton(root, text='1', variable=var, value=1)
```

> ⚡ **Важно!**  
> Все радиокнопки в группе используют **одну переменную**. Только одна кнопка может быть выбрана.

---

## Упаковщики (менеджеры геометрии)

> 📦 **Три способа упаковки**  
> В tkinter есть три упаковщика: `pack()`, `place()`, `grid()`. Нельзя смешивать их для одного родителя!

### pack()

```python
button1.pack(side='left')  # разместить слева
```

> 🧭 **Параметры side**  
> - `'left'` — слева  
> - `'right'` — справа  
> - `'top'` — сверху (по умолчанию)  
> - `'bottom'` — снизу

### place()

```python
button1.place(x=100, y=50, width=200, height=30)
```

> 🎯 **Точное позиционирование**  
> `place()` даёт полный контроль, но не адаптируется к изменению размера окна.

### grid()

```python
entry1.grid(row=0, column=0, columnspan=3)
```

> 📊 **Сетка**  
> - `row` — номер строки  
> - `column` — номер столбца  
> - `columnspan` — сколько столбцов занимает виджет  
> - `sticky` — "приклеивание" к стороне (`'n'`, `'s'`, `'w'`, `'e'`)

---

## Привязка событий

```python
виджет.bind('<событие>', функция_обработчик)
```

> 🖱️ **События мыши**

| Событие | Что делает |
|---------|------------|
| `<Button-1>` | Левая кнопка мыши |
| `<Button-2>` | Средняя кнопка |
| `<Button-3>` | Правая кнопка |
| `<Double-Button-1>` | Двойной клик |
| `<Motion>` | Движение мыши |

> ⌨️ **События клавиатуры**

| Событие | Что делает |
|---------|------------|
| `<Return>` | Enter |
| `<Control-c>` | Ctrl+C |
| `<F1>` | F1 |
| `<a>` | Клавиша A |

### Функция-обработчик

```python
def leftclick(event):
    print(f'Координаты: {event.x}, {event.y}')
```

> 🎁 **Атрибуты event**  
> - `event.x`, `event.y` — координаты мыши  
> - `event.widget` — виджет, на котором произошло событие  
> - `event.keysym` — название нажатой клавиши  

---

## Продвинутые виджеты

### Scale (Шкала/Ползунок)

```python
scale = Scale(root, orient=HORIZONTAL, length=300, 
              from_=50, to=80, tickinterval=5, resolution=5)
```

> ⚙️ **Параметры Scale**  
> - `from_` — минимальное значение (с подчёркиванием!)  
> - `tickinterval` — интервал между метками  
> - `resolution` — шаг перемещения

### Scrollbar (Полоса прокрутки)

```python
scr1 = Scrollbar(root, command=text1.yview)
text1.configure(yscrollcommand=scr1.set)
```

> 🔄 **Двусторонняя связь**  
> Скроллбар управляет текстом, а текст управляет скроллбаром!

---

## Диалоговые окна

```python
from tkinter import messagebox
```

> 📢 **Типы окон**

```python
messagebox.showinfo('Заголовок', 'Сообщение')      # информация
messagebox.showwarning('Заголовок', 'Предупреждение')  # предупреждение
messagebox.showerror('Заголовок', 'Ошибка')        # ошибка
```

> ❓ **Окна с вопросами**

```python
answer = messagebox.askyesno('Вопрос', 'Вы уверены?')
# answer будет True или False
```

---

## Стикеры и заметки

> ⭐ **Лучшие практики**

- ✅ Всегда используйте `mainloop()` в конце программы
- ✅ Давайте виджетам осмысленные имена
- ✅ Используйте `grid()` для сложных интерфейсов
- ✅ Не забывайте про отступы (`padx`, `pady`)

> ⚠️ **Частые ошибки**

- ❌ Забыли `mainloop()` — окно не появится
- ❌ Смешиваете `pack()` и `grid()` для одного родителя
- ❌ Не импортировали `messagebox` для диалогов
- ❌ Используете `from` вместо `from_` в Scale

> 💡 **Полезные советы**

| Проблема | Решение |
|----------|---------|
| Русские буквы | В Python 3 всё работает, в Python 2 нужен префикс `u` |
| Прозрачность | `root.attributes('-alpha', 0.9)` |
| Поверх всех окон | `root.attributes('-topmost', True)` |
| Иконка | `root.iconbitmap('icon.ico')` |

> 🚀 **Для быстрого старта**

```python
# Минимальная программа
from tkinter import *
root = Tk()
Label(root, text='Привет, мир!').pack()
root.mainloop()
```

> 📚 **Что почитать дальше**

- Официальная документация Python
- Книга "Python GUI Programming with Tkinter"
- Форум StackOverflow (тег [tkinter])

> 🎯 **Практические задания**

1. Создайте калькулятор
2. Напишите текстовый редактор
3. Сделайте игру "Крестики-нолики"
4. Разработайте менеджер паролей

---

## Примеры программ с комментариями

### Пример 1: Калькулятор (со стикерами)

```python
from tkinter import *

def calculate():
    """Функция вычисления результата"""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        # Выполняем операцию
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = 'Ошибка: деление на 0'
            else:
                result = num1 / num2
        else:
            result = 'Выберите операцию'
        
        label_result.config(text=f'Результат: {result}')
    except ValueError:
        label_result.config(text='Ошибка: введите числа')

# Создание главного окна
root = Tk()
root.title('Калькулятор')  # Заголовок окна
root.geometry('300x250')    # Размер окна
root.resizable(False, False)  # Запрещаем изменение размера

# Поля ввода
Label(root, text='Число 1:').grid(row=0, column=0, padx=5, pady=5)
entry1 = Entry(root, width=15)
entry1.grid(row=0, column=1, padx=5, pady=5)

Label(root, text='Число 2:').grid(row=1, column=0, padx=5, pady=5)
entry2 = Entry(root, width=15)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Выбор операции
Label(root, text='Операция:').grid(row=2, column=0, padx=5, pady=5)
operation_var = StringVar()
operation_var.set('+')  # Операция по умолчанию

operations = ['+', '-', '*', '/']
for i, op in enumerate(operations):
    Radiobutton(root, text=op, variable=operation_var, 
                value=op).grid(row=2, column=i+1, padx=2)

# Кнопка вычисления
Button(root, text='Вычислить', command=calculate).grid(
    row=3, column=0, columnspan=4, pady=10)

# Результат
label_result = Label(root, text='Результат:', font='Arial 12 bold')
label_result.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()
```

> 📌 **Комментарии к коду**  
> - `try/except` обрабатывает ошибки ввода  
> - `columnspan=4` растягивает кнопку на 4 колонки  
> - `resizable(False, False)` фиксирует размер окна

---

## Шпаргалка по основным командам

| Команда | Описание | Пример |
|---------|----------|--------|
| `Tk()` | Создание окна | `root = Tk()` |
| `Button()` | Кнопка | `Button(root, text='OK')` |
| `Label()` | Метка | `Label(root, text='Привет')` |
| `Entry()` | Поле ввода | `Entry(root, width=20)` |
| `pack()` | Простая упаковка | `widget.pack()` |
| `grid()` | Сеточная упаковка | `widget.grid(row=0, column=0)` |
| `bind()` | Привязка события | `widget.bind('<Button-1>', func)` |
| `get()` | Получение значения | `value = widget.get()` |
| `config()` | Изменение свойств | `widget.config(text='Новый')` |

> 🏁 **Заключение**  
> Tkinter — отличный выбор для создания GUI на Python. С помощью этого руководства вы сможете создавать свои первые приложения. Экспериментируйте, практикуйтесь и создавайте полезные программы!
