# get_doc.pyimport selenium

from selenium import webdriver
import time
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
import pandas as pd
import matplotlib.pyplot as plt
import re
import selenium


#df1 = pd.DataFrame(columns = ['poster','To','Date','MSG_NUM', "TEXT"])
df1 = pd.DataFrame()
browser = webdriver.Chrome()
browser.get("https://www.siliconinvestor.com/readmsg.aspx?msgid=33516744")
#time.sleep(0)

for i in range(37):
    url = browser.current_url
    req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
    response = urlopen(req, timeout=120)  
    soup = BeautifulSoup(response, 'html.parser')

    try:
        post_text = soup.find(id='intelliTXT').contents
    except AttributeError:
        post_text = None
        pass
    date_post = soup.find("td", text = re.compile(r'\d+/\d+/\d+')).contents
    people = soup.find_all(href=re.compile('profile.*'))
    msg_num = soup.find_all('input',{'name' : "msgnum"} )[0].get('value')
    result = []
    for c in people:
        result.extend(c)
    if len(result) == 2:
        poster, replied_to = result[1], result[0]
    else:
        replied_to, poster = 'NONE', result[0]
        
    #print(f'POSTER: {poster}\n REPLIED TO: {replied_to}\n Date: {date_post}\n \
         # MSG_NUM: {msg_num}\n POST TEXT: {post_text}\n')
    d = {'poster':poster, 'To': replied_to, 'Date': date_post, \
         'MSG_NUM': msg_num, "TEXT": str(post_text)}
    df = pd.DataFrame(d)
    df1 = df1.append(df, ignore_index=True)
    
    #time.sleep(2)
    doc = browser.find_element_by_link_text('Previous')
    doc.click()
browser.quit()
df1.to_csv('scraped.csv')

# headline_table = {}
# url = 'https://www.siliconinvestor.com/readmsg.aspx?msgid=704932' 
# req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'}) 
# response = urlopen(req)  
# soup = BeautifulSoup(response)

# post_text = (soup.find(id='intelliTXT').contents)

# poster = soup.find_all(href=re.compile('profile.*'))
# result = []
# for c in poster:
#     result.extend(c)
# print(result, post_text) 
# time.sleep(3)
# browser.quit()