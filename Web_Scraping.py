import sys

import requests
from bs4 import BeautifulSoup


def myfunc():
    print("This is a Price Finder APP")
    print("If you want to know about Apple iPhone 15 then type I15.")
    print("If you want to know about Apple iPhone 14 then type I14.")
    print("If you want to know about Samsung Galaxy S22 5G then type S22.")

myfunc()

while True:
    Check=input("Did you Understant?(Yes/No)" )
    if Check=="yes":
        break
    else:
        myfunc()
        

while True:
    User_input=str(input("Chooes one: (I15/I14/S22)"))
    if User_input=="I15":
        URL= "https:/yes/www.ideabeam.com/mobile/apple-iphone-15-price.html#gsc.tab=0&gsc.q=Apple%20iPhone%2015&gsc.sort="
        break
    elif User_input=="I14":
        URL="https://www.ideabeam.com/mobile/apple-iphone-14-price.html#gsc.tab=0&gsc.q=Apple%20iPhone%2014&gsc.sort="
        break
    elif User_input=="S22":
        URL= "https://www.ideabeam.com/mobile/samsung-galaxy-s22-5g-price.html#gsc.tab=0&gsc.q=Samsung%20Galaxy%20S22%205G&gsc.sort="
        break
    else:
        print("Your Input is wrong try agian")


header_input=str(input("Input your User-agent: (Go to chorme and search MY USER AGENT)"))
header = { "User-Agent" : "" }
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36

page = requests.get(URL,headers=header)
    
soup = BeautifulSoup(page.content,'html.parser')
title = soup.find(  class_="pricerange").get_text()
lowPrice = soup.find( class_="lowprice").get_text()
highPrice = soup.find( class_="highprice").get_text()
product = soup.find("h2").get_text()

print("")
print(product.strip())
print(title.strip() ,"Low_Price =" ,lowPrice,"HIGH_Price= ",highPrice)

   





