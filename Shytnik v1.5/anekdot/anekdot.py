import requests
from bs4 import BeautifulSoup
import pyautogui as pt

URL = "https://www.anekdot.ru/random/anekdot/"
HEADERS = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0", 
           "Accept" : "*/*"}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find(class_="text")

    print("Сейчас будет шутка, ждите")
    pt.alert(items.text, "shytka!", "ok")


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        
    else:
        print("А вот нет!")


parse()