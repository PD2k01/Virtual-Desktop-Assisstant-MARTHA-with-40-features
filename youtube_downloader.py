import os
import pyperclip
from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
from pyperclip import paste
from time import sleep

def download():

    sleep(2)
    click(x=607, y=53)
    value = hotkey("ctrl","c")
    value = pyperclip.paste()

    link = str(value)

    def downloaded(link):

        url = YouTube(link)
        video = url.streams.first()
        video.download("D:\\MARTHA\\youtube downloaded videos\\")

    downloaded(link)

    os.startfile("D:\\MARTHA\\youtube downloaded videos\\")

