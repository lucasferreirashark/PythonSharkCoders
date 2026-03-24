from tkinter import *

def corazul():
    root.configure(background="#3a75e2")

def corvermelho():
    root.configure(background="#e23c3c")

def coramarelo():
    root.configure(background="#d7e23c")

def corverde():
    root.configure(background="#94e23c")

root = Tk()
root.title('Color Changer')
root.geometry('500x400+400+100')
root.wm_resizable(width=False, height=False)

bt1 = Button(root, text='Azul', font='Arial 14 bold', command=corazul)
bt1.place(width=200, height=160, x=40, y=20)

bt2 = Button(root, text='Vermelho', font='Arial 14 bold', command=corvermelho)
bt2.place(width=200, height=160, x=260, y=20)

bt3 = Button(root, text='Amarelo', font='Arial 14 bold', command=coramarelo)
bt3.place(width=200, height=160, x=40, y=200)

bt4 = Button(root, text='Verde', font='Arial 14 bold', command=corverde)
bt4.place(width=200, height=160, x=260, y=200)

root.mainloop()