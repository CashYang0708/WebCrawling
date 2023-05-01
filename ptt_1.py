import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
url='https://www.ptt.cc/bbs/NBA/index.html'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
print(soup.prettify())
soup=soup.findAll('div',{'class':'title'})
print(soup,type(soup))
'''for i in soup:#soup為list型態
    a=i.find_all('a')#i為beautiful型態,a為list型態
    for j in a:
        print(j.string)
        print('https://www.ptt.cc'+j['href'])#取得href裏面的連結
for title in soup:
    if title.a!=None:
        print(title.a.text,type(title.a))#取得a標籤裡面的文字
for title in soup:
    try:
        print(title.a.text)
    except AttributeError as e:
        print(title.text)
        print(title.args)'''

def search_PttTitleLink(boardname):
    url='https://www.ptt.cc/bbs/'+boardname+'/index.html'
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    soup=soup.find_all('div',{'class':'title'})
    for i in soup:
        a=i.find_all('a')
        for j in a:
            print('https://www.ptt.cc'+j['href'])
            
def search_PTTComment(url):
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    soup=soup.find('div',{'id':'main-content'})
    print(soup.text.split('--')[1])#用--將文章以及評論分開,取第1個

def search_PTTArticle(url):
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    soup=soup.find('div',{'id':'main-content'})
    print(soup.text.split('--')[0])#用--將文章以及評論分開,取第0個
    
def search_PTTTitle(url,printpage):
    while printpage>0:
        res=requests.get(url,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        div=soup.find_all('div',{'class':'title'})
        for title in div:
            try:
                print(title.a.text)
            except AttributeError as e:
                print(title.text)
        href=soup.find_all('div',{'class':'btn-group btn-group-paging'})
        for i in href:
            j=i.find_all('a')
            url='https://www.ptt.cc'+j[1]['href']
        printpage-=1
'''
用urllib
from urllib import request
url='網址'
headers={'User-Agent':電腦的useragent}
req=request.Request(url=變數url,headers=變數headers)
res=requset.urlopen(req)
print(res.read().decode('uft-8'))
'''

        
        
