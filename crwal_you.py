import requests
from bs4 import BeautifulSoup
import time
import urllib.request #
from selenium.webdriver import Chrome
import re
import  pandas as pd

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
asd=soup.find_all('div',{'id':'header-author'},{'class':'style-scope ytd-comment-renderer'})
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
cmt_ll=[]
count=0
for it in asd:
    it.find_all({'id':'author-text'})
for items in soup:
    div=items.find_all('yt-formatted-string',attrs={'class':'style-scope ytd-comment-renderer'})  #comment
    div2=items.find_all('span',attrs={'class':'style-scope ytd-comment-renderer'})
    for list2 in div2:
        if (list2.string != None) and (list2.string != 'VIEW'):
            ccc=(list2.string.replace('\n',"")).strip()
            if(ccc != '•') and (ccc != ''):
                cmt_ll.append([ccc])
    for lists in div:
        if (lists.string != None) and (lists.string != 'VIEW')and (lists.string!=''):
            cmt=(lists.string.replace('\n',"")).strip()
            if(cmt != ''):
                cmtlist.append([cmt])

casd={"comment" : cmtlist , "comment_id" : cmt_ll}
print(casd)
for t in casd:
    print(t)
    print("----------------------------------------------------")

#print(cmtlist)
print(len(cmtlist))
print(len(cmt_ll))

for i in range(len(cmtlist)):
    print(cmtlist[i])
    print(cmt_ll[i])

'''
frame=pd.DataFrame(casd)
print(frame)
frame.to_csv("frame2.csv",mode="w",encoding="utf-8-sig")
'''
