from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep

def whatsapp(name, message):

    startfile("C:\\Users\\Pratim\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=278, y=114)
    sleep(1)
    write(name)
    sleep(3)
    click(x=181, y=241)
    sleep(5)
    click(x=653, y=694)
    write(message)
    press("enter")



def whatsappCall(name):
    startfile("C:\\Users\\Pratim\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=278, y=114)
    sleep(1)
    write(name)
    sleep(3)
    click(x=181, y=241)
    sleep(5)
    click(x=1207, y=54)

def whatsappVideoCall(name):
    startfile("C:\\Users\\Pratim\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=278, y=114)
    sleep(1)
    write(name)
    sleep(3)
    click(x=181, y=241)
    sleep(5)
    click(x=1158, y=59)
    







