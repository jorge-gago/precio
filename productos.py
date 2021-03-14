import requests as req
import extrac
import datetime
import base

hdr = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}


def llamadas_url(url , headers = hdr):   
    urls = req.get( url, headers = hdr )
    data = urls.text

    return data

class producto():

    def __init__(self):
        self.nombre_pro = ""
        self.url_producto = ""
        self.data_url = ""
        self.nombre = ""
        self.precio = "00.00"
        self.foto = ""
        self.deseado = "00.00"
        self.pre_min = "--.--"
        self.pre_max = "--.--"
        self.precios = [[ 0, 0]]
        self.page = ""

    def change(self): # llama los datos de base y los pasa a object
        pass

    def  urls(self, url):
        self.url_producto = url
        self.data_url = llamadas_url(self.url_producto)
        self.page = extrac.web( url)

    def  precio_page(self):
        self.precio = extrac.precio(self.data_url, self.page).replace(".", ",")
        self.add_pre()

    def add_pre(self):
        fecha = datetime.date.today().strftime("%d/%m/%y")
        c = self.precio.find(",")+3
        precio_act = [ self.precio[:c], fecha ]

        if precio_act == self.precios[0]:
            pass
        else:
            self.precios.insert(0 , precio_act)
        if len(self.precios) > 10: 
            self.precios.pop() 
      
        print(self.precios)

    def  nombre_page(self):
        self.nombre = extrac.nombre(self.data_url, self.page).strip()

    def foto_page(self):
        foto_url = extrac.foto(self.data_url, self.page)[1:]
        #foto = pillow.imagen.open(foto_url, headers = hdr)
        #self.foto = foto

    def al (self):
        return self.page, self.url_producto, self.nombre, self.precio, self.deseado, self.pre_min, self.pre_max, self.precios, self.foto



    


    


    

# para prueba
if __name__ == "__main__":

    prueba = producto()
    prueba.urls('https://www.amazon.es/Moulinex-Multimoulinette-Compact-DJ300110-capacidad/dp/B00I96MAXC/ref=sr_1_50?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=moulinex&qid=1610394421&refinements=p_89%3AMoulinex&rnid=1692911031&s=kitchen&sr=1-50&th=1')
    
    prueba.precio_page()
    prueba.precio_page()
    prueba.nombre_page()

    for i in prueba.al():
        print(i)
"""
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
"""
    

 
