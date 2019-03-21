import requests
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
google_url = "https://www.google.com/search?q=python"
r = Request(google_url)
r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
response = urlopen(r)
soup = BeautifulSoup(response,'html.parser')
res = soup.find_all("div",class_="g")
x = 0

for i in res :
        x+=1
        div = i.find("div",class_="hJND5c") #提取div
        print(div)
        if div != None:
            print("第", x, "筆")
            cite = div.find("cite")
            print(cite.text)
        else :
            x -= 1
#----------
#---test---
#----------
# print(res[3])
# a = res[3].find("div",class_="hJND5c")
# print(a)
# if a!=None:
#     b = a.find("cite")
#     print(b)
#     print(b.text)
#else :
#   print("is none")
