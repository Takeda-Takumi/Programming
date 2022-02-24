from cProfile import label
import tkinter as tk


class Window(tk.Frame):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(text="UNCHI", name="fdsa")
        label.pack()
        print(label)


root = tk.Tk()

window = Window()
window.pack()
print(window)

tk.mainloop()