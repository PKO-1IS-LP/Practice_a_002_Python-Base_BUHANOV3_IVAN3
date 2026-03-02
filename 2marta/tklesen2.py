from tkinter import *
root=Tk()
listbox1=Listbox(root,height=10,width=20,selectmode=EXTENDED)
listbox2=Listbox(root,height=10,width=20,selectmode=SINGLE)
list1=[u"Юля",u"Вика",u"Нина",u"Женя"]
list2=[u"Саша",u"Ваня",u"Миша",u"Андрей"]
for i in list1:
    listbox1.insert(END,i)
for i in list2:
    listbox2.insert(END,i)
listbox1.pack()
listbox2.pack()
root.mainloop()