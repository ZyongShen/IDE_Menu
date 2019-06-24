from tkinter import *
import subprocess

class IDEMenu(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.makeButtons()

    def makeButtons(self):
        self.VStudio = Button(self, text="Visual Studio")
        self.VStudio["command"] = self.open_VS
        self.VStudio.grid()

        self.VSCode = Button(self, text = "VS Code")
        self.VSCode["command"] = self.open_VSC
        self.VSCode.grid()

        self.PyCharm = Button(self, text="PyCharm")
        self.PyCharm["command"] = self.open_PyC
        self.PyCharm.grid()

        self.IntelliJ = Button(self, text="IntelliJ")
        self.IntelliJ["command"] = self.open_IntJ
        self.IntelliJ.grid()

        self.CLion = Button(self, text="CLion")
        self.CLion["command"] = self.open_CL
        self.CLion.grid()

        self.AndStudio = Button(self, text="Android Studio")
        self.AndStudio["command"] = self.open_AStudio
        self.AndStudio.grid()


    def open_VS(self):
        # open Visual Studio
        subprocess.Popen("C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\devenv.exe")

    def open_VSC(self):
        # open VS Code
        subprocess.Popen("C:\Program Files\Microsoft VS Code\Code.exe")

    def open_PyC(self):
        # open PyCharm
        subprocess.Popen("C:\Program Files\JetBrains\PyCharm Community Edition 2018.3.3\bin\pycharm64.exe")

    def open_IntJ(self):
        # open IntelliJ
        subprocess.Popen("C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2018.2.5\bin\idea64.exe")

    def open_CL(self):
        # open CLion
        subprocess.Popen("C:\Program Files\JetBrains\CLion 2018.3.4\bin\clion64.exe")

    def open_AStudio(self):
        # open Android Studio
        subprocess.Popen("C:\Program Files\Android\Android Studio\bin\studio64.exe")

root = Tk()
root.title("IDE Menu")
root.geometry("300x400")

app = IDEMenu(root)
root.mainloop()
