from urllib import request as url_req
import requests as req

#buscar en pagina
nombre_page = '<span id="productTitle" class="a-size-large product-title-word-break">'
pre_temp = 'id="newBuyBoxPrice" class="a-size-base a-color-price header-price a-text-normal"'
pic = 'id="imgTagWrapperId"'

hdr = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

def llamadas_url(url = None, headers = hdr):
    urls = req.get( url, headers = hdr )

    data = urls.text
    return data

def precio(page):
    tramo = buscar(page, pre_temp)
    fin = (buscar(page, "€", tramo)) + tramo + 1
    ini = (buscar(page, ">", tramo)) + tramo + 1
    precio = page[ ini: fin]

    return precio

def nombre(page):
    nombre_p = buscar( page, nombre_page)
    nombre_ini = buscar(page, ">" , nombre_p) + nombre_p + 1
    nombre_f = buscar(page,'<' , nombre_ini) + nombre_ini 
    nombre_producto =(page[ nombre_ini: nombre_f]).replace("\n","")

    return  nombre_producto

def foto(page):
    fot = buscar( page, pic)
    ini = buscar( page, "data-old-hires=", fot) + fot + len("data-old-hires='")
    fin = buscar( page, ".jpg", ini) + ini + 4
    fotos = page[ ini: fin]

    return fotos

def buscar( data = " ", obj = "", posi = 0):
    buscar = data[ posi:].find(obj)
    return buscar




def pruebas(t2):

    print("nombre")
    print(nombre(t2))

    print("precio")
    print(precio(t2))

    print("foto")
    print(foto(t2))


    

# para prueba
if __name__ == "__main__":

    url = 'https://www.amazon.es/Moulinex-Multimoulinette-Compact-DJ300110-capacidad/dp/B00I96MAXC/ref=sr_1_50?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=moulinex&qid=1610394421&refinements=p_89%3AMoulinex&rnid=1692911031&s=kitchen&sr=1-50&th=1'

    pruebas(llamadas_url( url))

    print("---------------------------------------------------------------------------------------------------")

    url = 'https://www.amazon.es/Microsoft-Xbox-One-inal%C3%A1mbrico-embalaje/dp/B084TFVPW5/ref=sr_1_10?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=16BDERHHFYEWG&dchild=1&keywords=mando+xbox&qid=1611404680&refinements=p_89%3AMicrosoft&rnid=1692911031&s=videogames&sprefix=mando+xbo%2Caps%2C185&sr=1-10'

    pruebas(llamadas_url( url))

    print("------------------------------------------------------------------------------------------------------")

    url = 'https://www.amazon.es/Microsoft-QAT-00002-Mando-Xbox-Carbon/dp/B08FCXLB8Z/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=16BDERHHFYEWG&dchild=1&keywords=mando%2Bxbox&qid=1611404680&refinements=p_89%3AMicrosoft&rnid=1692911031&s=videogames&sprefix=mando%2Bxbo%2Caps%2C185&sr=1-1&th=1'

    pruebas(llamadas_url( url))

    print("-------------------------------------------------------------------------------------------------------")

    url = 'https://www.amazon.es/Controlador-PowerA-licencia-oficial-Windows/dp/B07NPY1YT5/ref=sr_1_20?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=mando%2Bxbox&qid=1613386373&s=videogames&sr=1-20&th=1'

    pruebas(llamadas_url( url))
    

 
