import urllib.parse  #url coding
import re #Match all Chinese with regular expressions
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

#Search google
def Search(question) :
    search_url = "https://www.google.com/search?q=" + question
    r = Request(search_url)
    r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    response = urlopen(r) #open url
    soup = BeautifulSoup(response, 'html.parser') #parse response
    div_g = soup.find_all("div", class_="g")
    count = 0
    for i in div_g:
        count += 1
        div = i.find("div", class_="hJND5c")  # get <div>
        title = i.find("h3")
        if div != None:  #get information is not None
            print("第", count, "筆資料")  #print information count
            print("文章標題:",title.text.strip()) #print title and remove all space
            cite = div.find("cite") #search url
            citeTextParsed = ParseQuestion(cite.text) #parse url
            if "https://" not in citeTextParsed:
                print("https://" + citeTextParsed)
            else :
                print(citeTextParsed)
        else:
            count -= 1
# url coding
def ParseQuestion(q) :
    for a in q:
        match = zh_pattern.search(a)
        if match:
            q = q.replace(a, urllib.parse.quote(a))
    q = q.replace(" ","%20")
    return q

if __name__ == '__main__' :
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')  # all Chinese with regular expressions
    question  = "林俊傑"  #input search content
    question  = ParseQuestion(question)
    Search(question)



