from tkinter import *
root = Tk()
text1 = Text(root,height=3,width=60)
scr1 = Scrollbar(root,command=text1.yview)
text1.configure(yscrollcommand=scr1.set)
text1.pack(side='left')
scr1.pack()
root.mainloop()
