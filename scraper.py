import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Greater-Noida")
c=r.content
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())

price=soup.find_all("div",{"class":"m-srp-card__price"})
#no_bhk=soup.find_all("span",{"class":"m-srp-card__title__bhk"})
summ=soup.find_all("div",{"class":"m-srp-card__summary js-collapse__content"})
det=soup.find_all("a",{"class":"m-srp-card__title"})
l=[]
for x in range(len(price)):
    d={}
    #print("---------------------")
    #print("Price = "+price[x].text)
    d["Price"]=price[x].text
    d["No. of BHK"]=no_bhk=det[x].find("span",{"class":"m-srp-card__title__bhk"}).text.replace("\n","")
    d["Address"]=add=det[x].text.replace(no_bhk,"").replace("\n","").replace("for Sale","").replace("in","").strip()
    #print(det[x].text)
    d["Summary"]=summ[x].text.replace("\n\n\n","|").replace("\n"," ").replace("\xa0"," ")
    #print(no_bhk)
    #print(add)
    #print("Info Summary")
    #print(area[x].text.replace("\n\n","\n"))
    l.append(d)

import pandas
df=pandas.DataFrame(l)
print(df)
df.to_csv("Ouput.csv")
