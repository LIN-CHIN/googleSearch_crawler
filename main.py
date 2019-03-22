import requests
from urllib.request import urlopen,Request
import urllib.parse  #url編碼
import re #使用正規表達匹配所有中文
from bs4 import BeautifulSoup
def Search(question) :
    search_url = "https://www.google.com/search?q=" + question
    r = Request(search_url)
    r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    response = urlopen(r)
    soup = BeautifulSoup(response, 'html.parser')
    res = soup.find_all("div", class_="g")
    x = 0
    for i in res:
        x += 1
        div = i.find("div", class_="hJND5c")  # 提取div
        print(div)
        if div != None:
            print("第", x, "筆")
            cite = div.find("cite")
            if "https://" not in cite.text:
                print("https://" + cite.text)
            else :
                print(cite.text)
        else:
            x -= 1
def ParseQuestion(q) :
    for a in q:
        match = zh_pattern.search(a)
        if match:
            q = q.replace(a, urllib.parse.quote(a))
    q = q.replace(" ","%20")
    return q  # 將中文編碼
#main
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')  #所有中文的正規表示式
question  = "台北-展覽" #丟出要搜尋的內容
aa = ParseQuestion(question)
Search(aa)




