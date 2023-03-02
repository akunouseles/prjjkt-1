from exmone import Bank
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url=('https://privatbank.ua/kak-otpravit-dengi-za-granicu')
file = "auto.csv"


def pars(site =url):
    inf = [] #informacija
    res = requests.get(site)
    if res.status_code != 200:
        print ("oshibka")
    else:
        soup = bs(res.text, features="html.parser")
        soup_list = soup.find_all('article', class_='block-content block-macro full-page-tab')
        for i in soup_list:
           # name = soup.find("article", class_="col-md-7 pull-left wr_inner") #
            name2 = soup.find_all("p", class_="")


            #name3= name2.__str__()
            #name4 = name3.split("<a>")
            #name5 = name4.__str__()
            #name6 = name5.split("</a>")




        #money = soup.find("span", class_="commission") # grivny
         # if namee or money :
            #     namee = namee.get_text(strip=True).replace(" ", "")
            #     money = money.get_text(strip=True).replace(" ", "")
            # else:
            #     print("eror2")
        inf.append({
            "название": name2

                #'money': money,


            })
    print(inf)
def chosee():
    print ("1-пополнить баланс \n "
           "2-снять средства \n"
           "3-просмотреть историю \n"
           "4-просмотреть баланс \n"
           "5-методы переводов (очень страшно не советую) \n")
    var = int(input())
    if var == 1:
        vtornik.pluss()
    if var == 2:
        vtornik.minuss()
    if var == 3:
        vtornik.historry()
    if var == 4:
        vtornik.balanceee()
    if var ==5:
        pars()
vtornik = Bank(name = "sybota")
while True:
    chosee()

