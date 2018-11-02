import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#used for websites that think you are a bot
headers = {'User-Agent': "info here"}


#start with base url, change url based on increments for page
# add in base url into brackets
url = []

for pg in range():#choose number of pages in website to scrape through
    url.append("company url from glass door{}.htm".format(pg))


#set empty list to gather all the information from the scrapping
date_item = []
overal_rating_item = []
title_item = []
location_item = []
job_title_item = []
pros_item = []
cons_item = []
advice_mgmt_item = []


#set loop for going through each page, taking the page html and parsing through it
for pg in url:
    print(pg)
    page = requests.get(pg, headers=headers).text
    soup = BeautifulSoup(page,"html.parser")
    #print(soup)
    reviews = soup.find_all("div",{"class":"hreview"})
    for item in reviews:
        #print(item)
        date = item.find("time", class_="date subtle small")["datetime"]
        date_item.append(date)
        overal_rating = item.find("span", class_= "value-title")["title"]
        overal_rating_item.append(overal_rating)
        title = item.find("span",class_="summary ").text
        title_item.append(title)
        location = item.find("span", class_="authorLocation")
        location_item.append(location)
        job_title = item.find("span", class_="authorJobTitle reviewer").text.strip()
        job_title_item.append(job_title)
        pros = item.find("p", class_=" pros mainText truncateThis wrapToggleStr").text.strip()
        pros_item.append(pros)
        cons = item.find("p", class_=" cons mainText truncateThis wrapToggleStr").text.strip()
        cons_item.append(cons)
        adviceMgmt = item.find("p", class_=" adviceMgmt mainText truncateThis wrapToggleStr")
        advice_mgmt_item.append(adviceMgmt)

## Make sure to place code in try/except block. I didn't need it for this scrape but always
#good to have since you are webscraping. 

#count list items on how much data items were scrapped from the site
print(len(date_item))
print(len(overal_rating_item))
print(len(job_title_item))
print(len(title_item))
print(len(pros_item))
print(len(cons_item))
print(len(location_item))
print(len(advice_mgmt_item))


#save list as a data frame for additional cleaning
company_reviews = pd.DataFrame({
    "Date":date_item,
    "Rating":overal_rating_item,
    "Job Title":job_title_item,
    "Summary":title_item,
    "Location":location_item,
    "Pro Comments":pros_item,
    "Con Comments":cons_item,
    "Advice to Mgmt":advice_mgmt_item
})


company_reviews.head()


#send to csv for exporting data
company_reviews.to_csv("company_reviews.csv", header=True)

