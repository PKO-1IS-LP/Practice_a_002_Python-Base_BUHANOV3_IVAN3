import tkinter as tk

#
window = tk.Tk()
window.title("Моё яркое приветствие")
window.geometry("500x200")
window.configure(bg="#FFFACD")  
label1 = tk.Label(
    window,
    text="HELLO WORLD!",
    font=("Impact", 48, "bold"),
    fg="#800080", 
    bg="#FFFACD"   
)
