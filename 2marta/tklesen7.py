from tkinter import *  # tkinter с маленькой буквы для Python 3
root = Tk()

def getV(event):  # Добавлен параметр event
    a = scale1.get()
    print("Значение", a)  # Скобки для print в Python 3

scale1 = Scale(root, orient=HORIZONTAL, length=3000, from_=0, to=800, tickinterval=25, resolution=1)
button1 = Button(root, text=u"Получить значение")
scale1.pack()
button1.pack()
button1.bind("<Button-1>", getV)

root.mainloop()