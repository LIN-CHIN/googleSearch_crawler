import requests
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
search_url = "https://www.google.com/search?q=python"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"}
res = requests.get(search_url, headers=headers)
soup = BeautifulSoup(res.content,'html.parser')
class_g = soup.find_all("div",class_="g")
try:
    for a in class_g :
        title = a.find("h3").text
        url = a.find("cite").text
        if "https://" not in url :
            url = "https://" + url
        print("標題:" , title)
        print("網址:",url)
except AttributeError:
    print('none')