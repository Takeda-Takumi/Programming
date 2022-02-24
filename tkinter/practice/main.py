
#外部ライブラリ
import tkinter as tk
from tkinter import ttk

#自作クラス
from Timetable import Timetable

class Application(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master)
        self.pack()
        self.master.geometry("1000x1000")
        self.master.title("Main Window")
        self.create_widgets()

    def create_widgets(self):
        frameForTimetable = tk.Frame()
        frameForTimetable.pack()
        timetable = Timetable(frameForTimetable)
        timetable.pack()



def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
