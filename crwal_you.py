import requests
from bs4 import BeautifulSoup
import time
import urllib.request #
from selenium.webdriver import Chrome
import re


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt


delay=3
browser=Chrome()
browser.implicitly_wait(delay)

start_url="https://www.youtube.com/watch?v=TMFW3F5hJ9o&list=PLfI752FpVCS8_5t29DWnsrL9NudvKDAKY&index=3&t=0s"
browser.get(start_url)
body=browser.find_element_by_tag_name('body')

num_of_pagedowns=3
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns-=1
soup=BeautifulSoup(browser.page_source,'html.parser')
info1 = soup.find('div',{'id':'info-contents'})
comm=soup.find('ytd-comments',{'id':'comments'})
comment1 = soup.find('yt-formatted-string', {'class': 'count-text style-scope ytd-comments-header-renderer'}).text
comment2 = comm.findAll('yt-formatted-string', {'class': 'style-scope ytd-comment-renderer'})
title = info1.find('h1',{'class':'title style-scope ytd-video-primary-info-renderer'}).text #영상제목
view =info1.find('yt-view-count-renderer',{'class':'style-scope ytd-video-primary-info-renderer'}).find_all('span')[0].text #영상 조회수
like = info1.find('div',{'id':'top-level-buttons'}).find_all('yt-formatted-string')[0].text #좋아요수
unlike = info1.find('div',{'id':'top-level-buttons'}).find_all('yt-formatted-string')[1].text #싫어요수
date = soup.find('span',{'class':'date style-scope ytd-video-secondary-info-renderer'}).text#영상업로드날
youtube_info={"title":title, "view":view,"like":like,"unlike":unlike,"date":date}

print("youtube_info")
print(youtube_info)
#print(comment1)
#print(comm)
#print(title)
#print(view)
#print(like)
#print(unlike)
#print(date)
cmtlist=[]
count=0
for items in soup:
    div=items.find_all('yt-formatted-string',attrs={'id':'content-text'})
    #print(div)
    for lists in div:
        if lists != None:
            try:
                cmt=lists.string
                cmtlist.append([cmt])
            except TypeError as e:
                pass
            else:
                pass

for t in cmtlist:
    print(t)
    print("----------------------------------------------------")