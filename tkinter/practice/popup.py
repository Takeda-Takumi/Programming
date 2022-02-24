import tkinter as tk
import tkinter.font as f
import subjects as sb

from tkinter import ttk

class detailWin():

    def __init__(self, root, subject = None):
        self.root = root
        self.win = None
        if subject == None:
            self.subject = sb.subject()
        else:
            self.subject = subject

    def hasWin(self):
        return ( not self.win ==  None and (self.win.winfo_exists()) )

    def get(self):
        return self.subject

    def makeWin(self):
        if self.hasWin():
            self.destory()
        self.win = tk.Toplevel(self.root)
        self.win.title("SubWindow")
        self.win.geometry(f"400x600+100+100")
        self.win.attributes("-topmost", True)


        s = ttk.Style()
        s.theme_use("clam")

        frame1 = tk.Frame(self.win, bg = "MediumPurple1", bd = 3, relief = tk.GROOVE)
        frame2 = tk.Frame(self.win, bg = "grey19", bd = 5)
        frame3 = tk.Frame(self.win, bg = "grey19", bd = 5)
        commands = tk.Frame(self.win, bg = "black", relief = tk.GROOVE,  bd = 3)
        frame1.pack( ipadx = 20, fill = tk.X)
        frame2.pack( ipady = 10, fill = tk.X)
        frame3.pack( expand = True, ipady = 10, fill = tk.BOTH)
        commands.pack( side=tk.BOTTOM, fill = tk.X, ipadx = 3)

        label1 = tk.Label(frame1, text="科目名", bg = "MediumPurple1", font = ("", 20))
        label1.pack(side=tk.LEFT, padx = 20)
        entory1 = tk.Entry(frame1, font = ("", 20), bg="lightslateblue", relief=tk.SOLID)
        entory1.insert(0, self.subject.name)
        entory1.pack(side=tk.LEFT, fill = tk.X, padx = 20)

        label2 = tk.Label(frame2, text="memo", bg = "ghostwhite", font = ("Century", 12))
        label2.pack(side=tk.TOP, anchor=tk.NW, pady = 10, padx = 10)
        textBox = tk.Text(frame2, bg = "ghostwhite", font=("HGSｺﾞｼｯｸM", 13), height = 8)
        textBox.insert(tk.END, self.subject.memo)
        textBox.pack(side=tk.LEFT, anchor=tk.SW,fill = tk.X, padx = 5, pady= 2)

        Label3 = tk.Label(frame3, text="課題一覧", bg = "MediumPurple1", bd=3, font=("HGSｺﾞｼｯｸE", 15), relief = tk.GROOVE)
        Label3.pack(fill = tk.BOTH)


        def restore():
            name = entory1.get()
            memo = textBox.get(1.0, tk.END)
            self.subject.name = name
            self.subject.newMemo(memo)

        bt_restore=tk.Button(commands, text="保存", bg="ghostwhite", font=("", 15), command=restore)
        bt_restore.pack(side=tk.LEFT)

    def destory(self):
        if self.hasWin():
            self.win.destroy()
            self.win = None

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("1000x600")

    dw = detailWin(root)
    but1 = tk.Button(root, text = "サブウィンドウ表示", command = dw.makeWin)
    but1.pack()

    root.mainloop()
