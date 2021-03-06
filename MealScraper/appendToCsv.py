import csv
from os import path
from datetime import datetime

def append(url, menu):
    if(not path.exists("results.csv")):
        open("results.csv",'x')
        with open("results.csv",'a') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["item","url","Date"])
    
    current = datetime.now()
    with open("results.csv",'a') as csvFile:
        writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in menu:
            writer.writerow([item,url,current])