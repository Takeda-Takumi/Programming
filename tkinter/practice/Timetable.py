#時間割のウィジェットを定義するクラスです

#外部ライブラリ
import tkinter as tk
from tkinter import LEFT, ttk
from turtle import width

#自作ライブラリ
from lesson import Lesson
from popup import detailWin


class Timetable():

    def __init__(self, master=None, cnf={}, **kw):
        # super().__init__(master)
        # self.pack()
        
        self.dw = detailWin(master)

        self.lessons = [Lesson(name="unchi") for i in range(5)]


        self.createWidgets()

    def createWidgets(self):
        #曜日の表示
        frameForWeek = tk.Frame(self)
        frameForWeek.pack()
        buttonMonday = defaultSettigButton(frameForWeek, text = "Mon")
        buttonMonday.grid(column=0,row=0)
        buttonTuesday = defaultSettigButton(frameForWeek, text = "Tue")
        buttonTuesday.grid(column=1,row=0)


        for i in range(5):
            self.lessons[i].pack()
            self.lessons[i].bind_all("<1>", self.call_detailwindow)
        #授業コマの表示
        # frameForLesson = tk.Frame(self)
        # frameForLesson.pack()
        # lesson1 = Lesson(frameForLesson)
        # lesson1.pack(side=LEFT, padx=10)
        # lesson2 = Lesson(frameForLesson)
        # lesson2.pack(side=LEFT, padx=10)

    def call_detailwindow(self, event):
        print(event.widget)
        pass




class defaultSettigButton(tk.Button):
    def __init__(self,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",14),height=2, width=4, relief="raised")

if __name__ == "__main__":
    root = tk.Tk()
    timetable = Timetable()
    timetable.mainloop()
