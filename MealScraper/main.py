from appendToCsv import append
from scraper import printItems, getItems
import os
import datetime

dt = datetime.datetime.today()

#test week day
if dt.weekday() > 4:
    cr_breakfast="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    cr_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    cr_dinner="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1384&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)


    pen_breakfast="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    pen_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    pen_dinner="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1384&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)

    #build arrays
    breakfast_array=[cr_breakfast, pen_breakfast]
    lunch_array=[cr_lunch, pen_lunch]
    dinner_array=[cr_dinner, pen_dinner]

elif dt.weekday() == 4:
    russ_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1760&storeIds=&mode=Daily&periodId=1383&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    cr_breakfast="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    cr_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1383&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    cr_dinner="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1384&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)


    pen_breakfast="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    pen_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1383&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    pen_dinner="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1384&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)  

    #build arrays
    breakfast_array=[cr_breakfast, pen_breakfast]
    lunch_array=[russ_lunch, cr_lunch, pen_lunch]
    dinner_array=[cr_dinner, pen_dinner]

else:
    russ_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1760&storeIds=&mode=Daily&periodId=1383&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    russ_dinner="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1760&storeIds=&mode=Daily&periodId=1384&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)

    cr_breakfast="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    cr_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1383&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    cr_dinner="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=14812&storeIds=&mode=Daily&periodId=1384&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)


    pen_breakfast="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1382&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    pen_lunch="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1383&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)
    pen_dinner="https://udel.campusdish.com/LocationsAndMenus/CaesarRodneyFreshFoodCompany?locationId=1729&storeIds=&mode=Daily&periodId=1384&date="+str(dt.month)+"%2F"+str(dt.day)+"%2F"+str(dt.year)  

    #build arrays
    breakfast_array=[cr_breakfast, pen_breakfast]
    lunch_array=[russ_lunch, cr_lunch, pen_lunch]
    dinner_array=[russ_dinner, cr_dinner, pen_dinner]


#for-loop, need to separate for different meal times for different resultfiles
for url in breakfast_array:
    print("URL is: "+url)
    printItems(url)
    append(url,getItems(url),"b_results.csv")

for url in lunch_array:
    print("URL is: "+url)
    printItems(url)
    append(url,getItems(url),"l_results.csv")

for url in dinner_array:
    print("URL is: "+url)
    printItems(url)
    append(url,getItems(url),"d_results.csv")
