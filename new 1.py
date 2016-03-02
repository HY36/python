from tkinter import *
class App(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWidgets()
    def creatWidgets(self):
        self.button = Button(self,text='Quit', fg='red', command = self.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(self,text='Hello',command = self.say_hi)
        self.hi_there.pack(side=LEFT)
    def say_hi(self):
        print('hi there, everyone!')

app = App()
app.master.title('Hi')
app.mainloop()