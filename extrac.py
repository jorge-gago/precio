import requests as req
from bs4 import BeautifulSoup


hdr = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

paginas = {
     "amazon":{ "nombre":"productTitle", "precio": "priceblock_ourprice", "stock": "availability", "foto":"imgTagWrapper"}}


def llamadas( url, headers = hdr):
    data = req.get( url, headers = hdr )

    return data

def llamadas_url(url):
    urls = llamadas(url)
    soup = BeautifulSoup( urls.content, "html.parser")
    page = pagina(url)
    buscar = paginas[page]
    try:
        precio = soup.find( id = buscar[ "precio"]).get_text()
    except:
        disponibilidad = soup.find( id = buscar[ "stock"]).get_text()
        precio = disponibilidad.strip()
    nombre = soup.find( id = buscar["nombre"]).get_text().strip()
    fotos = str(soup.find( class_ = buscar["foto"]))
    foto = fotos.find("data-old-hires") + len("data-old-hires  ")
    fin = fotos[foto:].find(".jpg") + len(".jpg")+ foto
    url_foto = fotos[foto: fin]

    return nombre, precio, url_foto

def pagina(url):
    ini = url.find("www.") + len("www.")
    fin = url[ini:].find(".") + ini  
    page = url[ini:fin]
   
    return page

if __name__ == "__main__":

    url = 'https://www.amazon.es/Moulinex-Multimoulinette-Compact-DJ300110-capacidad/dp/B00I96MAXC/ref=sr_1_50?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=moulinex&qid=1610394421&refinements=p_89%3AMoulinex&rnid=1692911031&s=kitchen&sr=1-50&th=1'

    #url = 'https://www.amazon.es/Microsoft-Xbox-One-inal%C3%A1mbrico-embalaje/dp/B084TFVPW5/ref=sr_1_10?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=16BDERHHFYEWG&dchild=1&keywords=mando+xbox&qid=1611404680&refinements=p_89%3AMicrosoft&rnid=1692911031&s=videogames&sprefix=mando+xbo%2Caps%2C185&sr=1-10'

    nom, pre, fot = llamadas_url(url)
    print(pre)


