from appendToCsv import append
from scraper import printItems, getItems

f = open("urls","r")
urls = f.readlines()

for url in urls:
    print("URL is: "+url)
    printItems(url)
    append(url,getItems(url))

