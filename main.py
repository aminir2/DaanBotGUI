import selenium.common.exceptions
from selenium import webdriver
from time import sleep
import tkinter as tk
from tkinter import messagebox
import pygame

def Window():
    window = tk.Tk()
    window.geometry('299x399')
    window.iconbitmap('icon.ico')
    window.title("Daan Bot Beta")
    window.resizable(False, False)
    background = tk.PhotoImage(file="background.png")
    bg = tk.Label(window, image=background)
    bg.place(x=0, y=0)
    universities = {
        "1": 'iauctb',
        "2": 'iau-tnb'
    }
    option_lable = tk.Label(text="لیست دانشگاه ها", bg="#80bfff")
    option_lable.place(x=100, y=4)
    options = tk.StringVar(window)
    options.set(universities["1"])
    uniOptions = tk.OptionMenu(window, options, *universities.values())
    uniOptions.place(x=115, y=24)
    lable1 = tk.Label(text="کد دانشجویی", bg="#80bfff")
    lable1.place(x=4, y=60)
    ent1 = tk.Entry()
    ent1.get()
    ent1.place(x=90, y=60)
    lable1 = tk.Label(text="رمز", bg="#80bfff")
    lable1.place(x=30, y=90)
    ent2 = tk.Entry()
    ent2.get()
    ent2.place(x=90, y=90)
    btn = tk.Button(fg="blue", text="ورود", width=10, height=3)
    btn['command'] = (lambda:
                      doing(ent1, ent2, options))
    btn.place(x=110, y=140)
    window.mainloop()

def doing(ent1, ent2, options):
    username = ent1.get()
    password = ent2.get()
    university = options.get()
    browser = webdriver.Chrome(executable_path="PATH OF YOUR DRIVER WHICH YOU DOWNLOADED")
    browser.get(f"http://{university}.daan.ir")
    browser.find_element_by_xpath("//a[contains(text(), 'شناسایی')]").click()
    browser.find_element_by_xpath('//input[@name="identification_number"]').send_keys(username)
    browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    browser.find_element_by_xpath('//button[@type="submit"]').click()
    browser.find_element_by_xpath(f"//a[contains(text(), 'جلسات من')]").click()
    while True:
        browser.find_element_by_xpath(
            f'//html//body//div[@class="main col-12"]//div[@class="row justify-content-center"]//section[@id="session-list"]//a[@class="btn btn-info "]').click()
        try:
            if browser.current_url != f'http://{university}.daan.ir/session-list#session-list':
                pygame.mixer.init()
                pygame.mixer.music.load("alert.mp3")
                pygame.mixer.music.play(loops=0)
                messagebox.showwarning(title="وضعیت ورود استاد", message="استاد وارد شد!")
                break
            elif browser.find_element_by_xpath(
                    f'//html//body//div[@class="main col-12"]//div[@class="row justify-content-center"]//section[@id="session-list"]//a[@class="btn btn-info "]'):
                browser.find_element_by_xpath(
                    f'//html//body//div[@class="main col-12"]//div[@class="row justify-content-center"]//section[@id="session-list"]//a[@class="btn btn-info "]').click()
                continue
        except selenium.common.exceptions.NoSuchElementException:
            pass

Window()
