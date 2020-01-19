# -*- coding: utf-8 -*-
#Instagra scrapper can find follwers,following and posts of a account
#helpful if someone blocked you

import requests
from bs4 import BeautifulSoup

URL="https://www.instagram.com/{}/"

def scrape(username) :
    full_url=URL.format(username)#create the url 
    r=requests.get(full_url)
    s=BeautifulSoup(r.text,"lxml")

    tag=s.find("meta",attrs={"name":"description"})
    text=tag.attrs['content']
    main_text=text.split("-")[0]

    return main_text


USERNAME="ingeniumseas"  #please follow me  @parthpatel1470 or can enter other insta id 
data=scrape(USERNAME)
print(data)

#output
#475 Followers, 15 Following, 55 Posts 