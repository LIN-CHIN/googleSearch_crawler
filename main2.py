import requests
import urllib.parse
from bs4 import BeautifulSoup
q = "電影"
search_url = "https://www.google.com/search?q="
q = urllib.parse.quote(q)
search_url  += q
print(search_url)
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"}
res = requests.get(search_url, headers=headers)
soup = BeautifulSoup(res.content,'html.parser')
class_g = soup.find_all("div",class_="g")
times = 0
try:
    for a in class_g :
        title = a.find("h3").text
        url = a.find("cite").text
        if "https://" not in url :
            url = "https://" + url
        print("標題:" , title)
        print("網址: ",url)
except AttributeError:
    print('none')
