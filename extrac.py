import requests as req
from bs4 import BeautifulSoup


hdr = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

data_page = []

def llamadas( url, headers = hdr):
    data = req.get( url, headers = hdr )

    return data

def llamadas_url(url):
    urls = llamadas(url)
    soup = BeautifulSoup( urls.content, "html.parser")
    for i in soup.findAll(True, {"id":True}):
        data_page.append(i["id"])

    #price = soup.find(id = "price").get_text()
    #print(price)
    dats()

def dats():
    for i in range(len(data_page)):
        print(data_page[i])

if __name__ == "__main__":

    url = url = 'https://www.amazon.es/Moulinex-Multimoulinette-Compact-DJ300110-capacidad/dp/B00I96MAXC/ref=sr_1_50?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=moulinex&qid=1610394421&refinements=p_89%3AMoulinex&rnid=1692911031&s=kitchen&sr=1-50&th=1'

    llamadas_url(url)


