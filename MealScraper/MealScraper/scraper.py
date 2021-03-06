from bs4 import BeautifulSoup
from urllib.request import urlopen

def printItems(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    menu = soup.find_all("li",class_="menu__item")

    for item in menu:
        print("______________")
        try:
            itemName = item.find("a",class_="viewItem").getText()
            print(itemName)
        except:
            try:
                itemName = item.find("span",class_="item__name").getText()
                print(itemName)
            except:
                print("N/A")

def getItems(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    menu = soup.find_all("li",class_="menu__item")
    arr = []

    for item in menu:
        try:
            itemName = item.find("a",class_="viewItem").getText()
            arr.append(itemName)
        except:
            try:
                itemName = item.find("span",class_="item__name").getText()
                arr.append(itemName)
            except:
                arr.append("N/A")
    return arr
