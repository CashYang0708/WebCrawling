import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
src = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(src, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
print(data)


import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title)
print(root.title.string)
title1= root.find("div", class_="title")
print(title1)
title2=root.find_all("div",class_="title")
print(title2)
for title in title2:
    if title.a != None:
        print(title.a.string)


ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"#網頁原始碼
request=req.Request(url,headers={"cookie":"over18=1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
#創立request物件附加request headers的資訊
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)
import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title)#抓到標籤還有裡面的文字
print(root.title.string)#抓到標籤裡的文字
titles=root.find_all("div", class_="title")#尋找class="title"的div標籤
print(titles)
for title in titles:
    if title.a!=None: #有找到div的a標籤
        print(title.a.string)
nextLink=root.find("a",string="‹ 上頁")
print(nextLink)
print(nextLink["href"])


import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req
def getData(url):
    request=req.Request(url,headers={"cookie":"over18=1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    title1=root.find_all("div", class_="title")#尋找class="title"的div標籤
    print(title1)#印出html type為list
    for title in title1:
        if title.a!=None:#如果html中的a標籤不是空的
            print(title.a.string)
    nextLink=root.find("a",string="‹ 上頁")
    print(nextLink)
    return nextLink["href"]
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<4:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1



