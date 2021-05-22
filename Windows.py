import tkinter as tk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
from functions import auto, otherclass


class Show:
    def __init__(self, WindowName=None, WindowSize="299x399", WindowIconPath=None, WindowTitle="Daan Bot", path=None,
                 text=None,
                 width=None, height=None, command=None,
                 place_x=None, place_y=None, index=None, insertText=None, backColor=None, backPath="background.png",
                 options1=None,
                 font=None,
                 value=None, fg=None):
        self.WindowName = WindowName
        self.WindowSize = WindowSize
        self.WindowIconPath = WindowIconPath
        self.WindowTitle = WindowTitle
        self.path = path
        self.text = text
        self.width = width
        self.height = height
        self.command = command
        self.place_y = place_y
        self.place_x = place_x
        self.index = index
        self.insertText = insertText
        self.backColor = backColor
        self.backPath = backPath
        self.options1 = options1
        self.value = value
        self.font = font
        self.fg = fg

    def defaultSettings(self):
        self.WindowName.geometry(f'{self.WindowSize}')
        self.WindowName.iconbitmap(f'{self.WindowIconPath}')
        self.WindowName.title(f"{self.WindowTitle}")
        self.WindowName.resizable(False, False)

    def background(self):
        global background
        background = ImageTk.PhotoImage(Image.open(self.backPath))
        bg = tk.Label(self.WindowName, image=background).place(x=0, y=0)

    def background2(self):
        global background2
        background2 = ImageTk.PhotoImage(Image.open(self.backPath))
        bg2 = tk.Label(self.WindowName, image=background2).place(x=0, y=0)

    def button(self):
        Button(self.WindowName, fg=self.fg, text=self.text, width=self.width, height=self.height,
               command=self.command).place(
            x=self.place_x, y=self.place_y)

    def label(self):
        Label(self.WindowName, text=f"{self.text}", bg=self.backColor, font=self.font).place(x=self.place_x,
                                                                                             y=self.place_y)

    def options(self):
        universities = {
            "1": 'iauctb',
            "2": 'iau-tnb',
            '3': "srbiau",
            '4': 'azad',
            '5': 'wtiau',
            '6': 'iauet',
        }
        OptionMenu(self.WindowName, self.options1, *universities.values()).place(x=self.place_x, y=self.place_y)

    def finish(self):
        self.WindowName.mainloop()


def mainPage():
    window = tk.Tk()
    run = Show(WindowName=window)
    run.defaultSettings()
    back = Show(WindowName=window)
    back.background2()
    btn = Show(WindowName=window, fg="blue", width=10, height=3, command=lambda: [AutoLoginPage()],
               text="ورود اتومات",
               place_x=110,
               place_y=120)
    btn.button()
    btn1 = Show(WindowName=window, fg="blue", width=15, height=3, command=lambda: (otherClasses()),
                text="ورود با شناسه‌ی جلسه",
                place_x=84,
                place_y=170)
    btn1.button()
    btn2 = Show(WindowName=window, fg="blue", width=10, height=3, command=window.destroy, text="خروج", place_x=110,
                place_y=250)
    btn2.button()
    finish = Show(WindowName=window)
    finish.finish()


def AutoLoginPage():
    window = Toplevel()
    run = Show(WindowName=window)
    run.defaultSettings()
    back = Show(WindowName=window)
    back.background()
    universities = {
        "1": 'iauctb',
        "2": 'iau-tnb',
        '3': "srbiau",
        '4': 'azad',
        '5': 'wtiau',
        '6': 'iauet',
    }
    option_lable = Show(WindowName=window, text="لیست دانشگاه ها", backColor="#80bfff", place_x=100, place_y=4)
    option_lable.label()
    options0 = StringVar(window)
    options0.set(universities["1"])
    uniOptions = Show(WindowName=window, options1=options0, place_x=115, place_y=24)
    uniOptions.options()
    myFont = font.Font(size=8)
    lable0 = Show(WindowName=window, text=" محل ChromeDriver", backColor='#80bfff', font=myFont, place_x=4, place_y=60)
    lable0.label()
    ent0 = Entry(window)
    ent0.insert(0, 'محل قرارگیری درایور را تایپ کنید.')
    ent0.place(x=90, y=60)
    lable1 = Show(WindowName=window, text="کد دانشجویی", backColor="#80bfff", place_x=4, place_y=90)
    lable1.label()
    ent1 = Entry(window)
    ent1.insert(1, 'کد دانشجویی خود را وارد کنید.')
    ent1.place(x=90, y=90)
    lable2 = Show(WindowName=window, text="رمز", backColor="#80bfff", place_x=30, place_y=120)
    lable2.label()
    ent2 = Entry(window)
    ent2.insert(2, 'رمز سامانه‌ی خود را وارد کنید.')
    ent2.place(x=90, y=120)
    btn = Show(WindowName=window, fg="blue", text="ورود", width=10, height=3,
               command=(lambda: auto(ent0, ent1, ent2, options0)), place_x=110,
               place_y=170)
    btn.button()
    btn0 = Show(WindowName=window, fg="blue", text="خروج", width=10, height=3, command=window.destroy, place_x=110,
                place_y=220)
    btn0.button()


def otherClasses():
    window = Toplevel()
    run = Show(WindowName=window)
    run.defaultSettings()
    back = Show(WindowName=window)
    back.background()
    universities = {
        "1": 'iauctb',
        "2": 'iau-tnb',
        '3': "srbiau",
        '4': 'azad',
        '5': 'wtiau',
        '6': 'iauet',
    }
    option_lable = Show(WindowName=window, text="لیست دانشگاه ها", backColor="#80bfff", place_x=100, place_y=4)
    option_lable.label()
    options0 = StringVar(window)
    options0.set(universities["1"])
    uniOptions = Show(WindowName=window, options1=options0, place_x=115, place_y=24)
    uniOptions.options()
    myFont = font.Font(size=8)
    lable0 = Show(WindowName=window, text=" محل ChromeDriver", backColor='#80bfff', font=myFont, place_x=4, place_y=60)
    lable0.label()
    ent0 = Entry(window)
    ent0.insert(0, 'محل قرارگیری درایور را تایپ کنید.')
    ent0.place(x=90, y=60)
    lable1 = Show(WindowName=window, text="کد دانشجویی", backColor="#80bfff", place_x=4, place_y=90)
    lable1.label()
    ent1 = Entry(window)
    ent1.insert(1, 'کد دانشجویی خود را وارد کنید.')
    ent1.place(x=90, y=90)
    lable2 = Show(WindowName=window, text="رمز", backColor="#80bfff", place_x=30, place_y=120)
    lable2.label()
    ent2 = Entry(window)
    ent2.insert(2, 'رمز سامانه‌ی خود را وارد کنید.')
    ent2.place(x=90, y=120)
    lable3 = Show(WindowName=window, text='شناسه‌ی جلسه', backColor='#80bfff', place_x=4, place_y=150)
    lable3.label()
    ent3 = Entry(window)
    ent3.insert(3, "شناسه‌ی جلسه را وارد کنید")
    ent3.place(x=90, y=150)
    lable4 = Show(WindowName=window, text='رمز جلسه', backColor='#80bfff', place_x=20, place_y=180)
    lable4.label()
    ent4 = Entry(window)
    ent4.insert(4, "رمز جلسه را وارد کنید")
    ent4.place(x=90, y=180)
    btn = Show(WindowName=window, fg="blue", text="ورود", width=10, height=3,
               command=(lambda: otherclass(ent0, ent1, ent2, ent3, ent4, options0)), place_x=110,
               place_y=230)
    btn.button()
    btn0 = Show(WindowName=window, fg="blue", text="خروج", width=10, height=3, command=window.destroy, place_x=110,
                place_y=280)
    btn0.button()
