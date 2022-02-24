# 授業1コマのウィジェットを定義するクラスです

#外部ライブラリ
from doctest import master
import tkinter as tk
from tkinter import LEFT, ttk
from turtle import left

from sklearn.linear_model import Ridge

#自作クラス
from popup import detailWin
import subjects as sb


class Lesson(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master)
        self.configure(bg="red")
        #self.configure(width=400, height=800)
        # self.configure(borderwidth=5)
        self.configure(relief="ridge")
        self.configure(padx=5, pady=5)
        self.pack()
         #fix データを仮で設定している
        memo = "・レポート課題3つ\n・林先生\n"
        subj = sb.subject("アルゴリズムとデータ構造")
        subj.newMemo(memo)
        self.detailWindow = detailWin(self, subj)
        
        self.createWidgets()

    def createWidgets(self):
        frameForSubjectName =  tk.Frame(self, bd = 3) #fix 変数名がよくない 科目名のフレーム
        frameForSubjectName.grid()
        subjectName = tk.Label(frameForSubjectName, text="科目名")
        subjectName.pack(padx=2, pady=2)

        # frameForCallDetailWindow = tk.Frame(self)
        # frameForCallDetailWindow.grid(padx=10, pady=10)
        # callDetailWindowButton = tk.Button(frameForCallDetailWindow, text='編集', command=self.callDetailWindow)
        # callDetailWindowButton.grid()

    # def callDetailWindow(self):
    #     pass
    #     print("詳細ウィンドウを表示")
    #     self.detailWindow.makeWin()





if __name__ == "__main__":
    root = tk.Tk()
    lesson = Lesson(master=root)
    lesson.mainloop()