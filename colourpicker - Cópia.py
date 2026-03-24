from tkinter import *

corAzul="#3a75e2"
corVermelho="#e23c3c"
corAmarelo="#d7e23c"
corVerde="#94e23c"

def definirFundoAzul():
    root.configure(background=corAzul)

def definirFundoVermelho():
    root.configure(background=corVermelho)

def definirFundoAmarelo():
    root.configure(background=corAmarelo)

def definirFundoVerde():
    root.configure(background=corVerde)

def definirTextoCorAtualAzul():
    apresentarCorAtual = Label(root, text="Azul", font="Arial 14 bold", background=corAzul)
    apresentarCorAtual.place(x=250,y=600)

def definirTextoCorAtualVermelho():
    apresentarCorAtual = Label(root, text="Vermelho", font="Arial 14 bold", background=corVermelho)
    apresentarCorAtual.place(x=250,y=600)

def definirTextoCorAtualAmarelo():
    apresentarCorAtual = Label(root, text="Amarelo", font="Arial 14 bold", background=corAmarelo)
    apresentarCorAtual.place(x=250,y=600)

def definirTextoCorAtualVerde():
    apresentarCorAtual = Label(root, text="Verde", font="Arial 14 bold", background=corVerde)
    apresentarCorAtual.place(x=250,y=600)

def botaoAzul():
    definirFundoAzul()
    definirTextoCorAtualAzul()

def botaoVermelho():
    definirFundoVermelho()
    definirTextoCorAtualVermelho()

def botaoAmarelo():
    definirFundoAmarelo()
    definirTextoCorAtualAmarelo()

def botaoVerde():
    definirFundoVerde()
    definirTextoCorAtualVerde()

root = Tk()
root.title('Color Changer')
root.geometry('500x800+400+100')
root.wm_resizable(width=False, height=False)

bt1 = Button(root, text='Azul', font='Arial 14 bold', command=botaoAzul, foreground=corAzul, background="white")
bt1.place(width=200, height=160, x=40, y=20)

bt2 = Button(root, text='Vermelho', font='Arial 14 bold', command=botaoVermelho, foreground=corVermelho, background="white")
bt2.place(width=200, height=160, x=260, y=20)

bt3 = Button(root, text='Amarelo', font='Arial 14 bold', command=botaoAmarelo, foreground=corAmarelo, background="white")
bt3.place(width=200, height=160, x=40, y=200)

bt4 = Button(root, text='Verde', font='Arial 14 bold', command=botaoVerde, foreground=corVerde, background="white")
bt4.place(width=200, height=160, x=260, y=200)

root.mainloop()