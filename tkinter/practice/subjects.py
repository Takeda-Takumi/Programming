import datetime

class assignment: #課題用クラス
    def __init__(self, name, datetime = None, format = "%Y/%m/%d %H:%M:%S"):
        self.name = name
        self.format = format
        if datetime == None:
            self.date = None
        else:
            date = self.setDate(datetime, self.format)

    def setDate(self, str, format = "%Y/%m/%d %H:%M:%S"):
        self.date = datetime.datetime.strptime(str, format)

    def setFormat(self, format):
        self.format = format

    def __str__(self):
        str = f"課題名: {self.name}\n"
        str += f"締め切り: {datetime.datetime.strftime(self.date, self.format)}"
        return str

class subject:
    def __init__(self,name = ""):
        self.name = name
        self.memo = ""
        self.asslist = []

    def newMemo(self, memo):
        self.memo = memo
    def addMemo(self, memo):
        self.memo += memo

    def addAss(self, ass):
        self.asslist.append(ass)

    def __str__(self):
        str = f"課題名: {self.name}\n"
        str = str + "メモ:\n" + self.memo
        str += "課題一覧\n"
        for i in self.asslist:
            str += i.__str__()
            str += "\n"
        return str


if __name__ == "__main__":

    def inputMemo():
        memo = ""
        print("メモを入力してください。( END で終了)" )
        while(True):
            str = input()
            if ( str == "END" ):
                break
            memo += str+"\n"
        return memo

    sub = subject("数理情報学2")
    sub.newMemo(inputMemo())
    sub.addAss(assignment("課題レポート1", "2020/10/5 23:55:00"))
    sub.addAss(assignment("課題レポート2", "2020/12/25 23:55:00"))

    print()
    print(sub)
