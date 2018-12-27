import datetime

class logger:

    def __init__(self):
        self.log = "\n"

        now = datetime.datetime.now()
        self.log += "<"
        self.log += now.strftime("%Y-%m-%d %H:%M")
        self.log += ">"

    def lgn(self, str):
        self.log +="\n"
        self.log +=str

    def savelog(self):
        fp = open("res/logs/log.txt", "a")
        fp.write(self.log)
        fp.close()
