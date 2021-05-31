import selenium.common.exceptions
from selenium import webdriver
from time import sleep
import pygame
from tkinter import messagebox


def auto(ent0, ent1, ent2, options):
    path = ent0.get()
    username = ent1.get()
    password = ent2.get()
    university = options.get()
    browser = webdriver.Chrome(executable_path=path)
    browser.get(f"http://{university}.daan.ir")
    browser.find_element_by_xpath(
        '//main[@class="main"]//div[@class="boxHolder"]//div[@class="loginBox"]//div[@class="row justify-content-center welcome"]//section[@class="content col-12 col-sm-12 col-md-12"]//div[@class="in"]//div[@class=" row buttonHolder"]//a[@class="btn btn-primary loginBtn col-lg-4 col-sm-12 col-xs-12"]').click()
    browser.find_element_by_xpath('//input[@id="identificationNumber"]').send_keys(username)
    browser.find_element_by_xpath('//input[@id="password"]').send_keys(password)
    browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    if browser.find_element_by_xpath(
            '//button[@class="btn examBtn contentBtn"]'):
        browser.find_element_by_xpath(
            '//button[@class="btn examBtn contentBtn"]').click()
    browser.find_element_by_xpath(
        '//main[@class="main"]//section[3]//div[@class="row"]//div[@class="col-lg-12"]//div[@class="tiles"][1]//a[@class="holder"]//div[@class="tileHolder meeting"]//div[@class="textHolder"]//h3').click()
    while True:
        try:
            if browser.current_url != f'http://{university}.daan.ir/session-list#session-list' and browser.current_url != f'http://{university}.daan.ir/session-list':
                pygame.mixer.init()
                pygame.mixer.music.load("alert.mp3")
                pygame.mixer.music.play(loops=0)
                messagebox.showwarning(title="وضعیت ورود استاد", message="استاد وارد شد!")
                sleep(120)
                exit()
            elif browser.current_url == f'http://{university}.daan.ir/session-list#session-list' or browser.current_url == f'http://{university}.daan.ir/session-list':
                browser.find_element_by_xpath('//a[@class="btn examBtn resultBtn"]').click()
                continue
        except selenium.common.exceptions.NoSuchElementException:
            browser.refresh()
            continue
        sleep(5)


def otherclass(ent0, ent1, ent2, ent3, ent4, options):
    path = ent0.get()
    username = ent1.get()
    password = ent2.get()
    university = options.get()
    class_code = ent3.get()
    class_pass = ent4.get()
    browser = webdriver.Chrome(executable_path=path)
    browser.get(f"http://{university}.daan.ir")
    browser.find_element_by_xpath(
        '//main[@class="main"]//div[@class="boxHolder"]//div[@class="loginBox"]//div[@class="row justify-content-center welcome"]//section[@class="content col-12 col-sm-12 col-md-12"]//div[@class="in"]//div[@class=" row buttonHolder"]//a[@class="btn btn-primary loginBtn col-lg-4 col-sm-12 col-xs-12"]').click()
    browser.find_element_by_xpath('//input[@id="identificationNumber"]').send_keys(username)
    browser.find_element_by_xpath('//input[@id="password"]').send_keys(password)
    browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    if browser.find_element_by_xpath(
            '//button[@class="btn examBtn contentBtn"]'):
        browser.find_element_by_xpath(
            '//button[@class="btn examBtn contentBtn"]').click()
    browser.find_element_by_xpath(
        '//main[@class="main"]//section[3]//div[@class="row"]//div[@class="col-lg-12"]//div[@class="tiles"][1]//a[@class="holder"]//div[@class="tileHolder meeting"]//div[@class="textHolder"]//h3').click()
    browser.find_element_by_xpath('//input[@id="id"]').send_keys(class_code)
    browser.find_element_by_xpath('//input[@id="password"]').send_keys(class_pass)
    browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    while True:
        try:
            if browser.current_url != f'http://{university}.daan.ir/session-list#session-list' and browser.current_url != f'http://{university}.daan.ir/session-list':
                pygame.mixer.init()
                pygame.mixer.music.load("alert.mp3")
                pygame.mixer.music.play(loops=0)
                messagebox.showwarning(title="وضعیت ورود استاد", message="استاد وارد شد!")
                sleep(120)
                exit()
            elif browser.current_url == f'http://{university}.daan.ir/session-list#session-list' or browser.current_url == f'http://{university}.daan.ir/session-list':
                browser.find_element_by_xpath('//input[@id="id"]').send_keys(class_code)
                browser.find_element_by_xpath('//input[@id="password"]').send_keys(class_pass)
                browser.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
                continue
        except selenium.common.exceptions.NoSuchElementException:
            browser.refresh()
            continue
        sleep(5)

