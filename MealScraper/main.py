from appendToCsv import append
from scraper import printItems, getItems
import os

dirLoc = os.path.dirname(os.path.abspath(__file__))
urlLoc = dirLoc + "/urls"
print(urlLoc)
f = open(urlLoc,"r")
urls = f.readlines()

for url in urls:
    print("URL is: "+url)
    printItems(url)
    append(url,getItems(url))

