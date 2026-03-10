import tkinter as tk

def test():
    print("Hello World!")

root = tk.Tk()
root.title("HelloWorld")
root.geometry("500x300+200+100")
root.wm_resizable(width=False, height=False)

button1 = tk.Button(root, text = "Button 1", command = test, font = "Time 14 bold")
button1.place(x = 50, y = 50)

button2 = tk.Button(root, text = "Button 2", font = "Time 14 bold")

root.mainloop()