import csv
from os import path
from datetime import datetime

def append(url, menu, file):
    if(not path.exists(file)):
        open(file,'x')
        with open(file,'a') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["item","url","Date"])
    
    current = datetime.now()
    with open(file,'a') as csvFile:
        writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in menu:
            writer.writerow([item,url,current])