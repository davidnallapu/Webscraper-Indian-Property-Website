import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Greater-Noida")
c=r.content
soup=BeautifulSoup(c,"html.parser")
price=soup.find_all("div",{"class":"m-srp-card__price"})
summ=soup.find_all("div",{"class":"m-srp-card__summary js-collapse__content"})
det=soup.find_all("a",{"class":"m-srp-card__title"})
l=[]#list for properties
for x in range(len(price)):
    d={}
    d["Price"]=price[x].text
    d["No. of BHK"]=no_bhk=det[x].find("span",{"class":"m-srp-card__title__bhk"}).text.replace("\n","")
    d["Address"]=add=det[x].text.replace(no_bhk,"").replace("\n","").replace("for Sale","").replace("in","").strip()
    d["Summary"]=summ[x].text.replace("\n\n\n","|").replace("\n"," ").replace("\xa0"," ")
    l.append(d)

import pandas
df=pandas.DataFrame(l)
print(df)
df.to_csv("Ouput.csv")
