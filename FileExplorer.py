from tkinter import *
import os


class Display:
    def __init__(self, window):
        self.window = window
        self.window.resizable(False, False)
        self.window.title('FileExplorer')
        self.window.geometry('1250x700')
        self.frame = Frame(root, bg='#000000')
        self.frame.pack()
        self.TextA = StringVar()
        self.TextA.set('Search on the search.')
        self.A = Entry(self.frame)
        self.A.pack(side='right')
        self.LabelA = Label(self.window, textvariable=self.TextA, height=4)
        self.LabelA.pack(side='bottom')
        self.TextB = StringVar()
        self.TextB.set('Create on the center.')
        self.B = Entry(self.frame)
        self.B.pack(side='right')
        self.LabelB = Label(self.window, textvariable=self.TextB, height=4)
        self.LabelB.pack(side='bottom')
        self.TextC = StringVar()
        self.TextC.set("Open on the left (folders with two words must have single quotes, ex: 'my Folder')")
        self.C = Entry(self.frame)
        self.C.pack(side='right')
        self.LabelC = Label(self.window, textvariable=self.TextC, height=4)
        self.LabelC.pack(side='bottom')
        self.label = None
        self.A.bind('<Return>', self.listDir)
        self.B.bind('<Return>', self.createdir)
        self.C.bind('<Return>', self.opendir)


    def listDir(self, *args):
        try:
            x = os.listdir(self.A.get())
            if len(x) >= 26:
                self.label = Label(self.window, text=x, font="Helvetica 10 bold", bg='blue')
                self.label.pack()
                self.window.resizable(True, False)
            elif len(x) < 25:
                self.label = Label(self.window, text=x, font="Helvetica 25 bold", bg='blue')
                self.label.pack()
        except FileNotFoundError:
            self.label = Label(self.window, text='Path Not Found.', font="Helvetica 25 bold", bg='blue')
            self.label.pack()

    def createdir(self, *args):
        os.open(self.B.get(), os.O_RDWR | os.O_CREAT, 0o666)

    def opendir(self, *args):
        a = "xdg-open " + self.C.get()
        try:
            x = os.listdir(self.A.get())
        except FileNotFoundError:
            self.label = Label(self.window, text='Path Not Found, or you have a Double Worded File.', font="Helvetica 25 bold", bg='blue')
            self.label.pack()
        os.system(str(a))

root = Tk()
root['bg'] = '#000000'
Display(root)
root.mainloop()