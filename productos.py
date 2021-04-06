import requests as req
import extrac
import datetime
import base

hdr = { 'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}


class producto():

    def __init__(self):
        self.nombre_pro = ""
        #self.url_producto = ""
        #self.data_url = ""
        self.nombre = ""
        self.precio = "00.00"
        self.foto = ""
        self.deseado = "00.00"
        self.pre_min = "--.--"
        self.pre_max = "--.--"
        self.precios = [[ 0, 0]]
        self.urls = ""
        #self.page = ""
        self.id_p = 0

    def change(self, data): # cambia los datos de object
        print(data)
        self.id_p = data[0]
        self.nombre_pro = data[1]
        self.nombre = data[3]
        self.foto = data[4]
        self.deseado = data[5]
        self.pre_min = data[7]
        self.pre_max = data[8]
        self.precios = data[9]
        self.urls = (data[2])
        self.precio_page()

    def  precio_page(self):
        self.precio = extrac.llamadas_url(self.urls)[1]
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

    def datos(self):
        self.nombre, self.precio, foto_data = extrac.llamadas_url( self.urls)
        self.foto_page(foto_data)
        self.add_pre()

    def foto_page(self, data = 0):
        if data:
            pass
        else:
            self.foto = " "

    def al (self):
        return self.urls, self.nombre, self.precio, self.deseado, self.pre_min, self.pre_max, self.precios, self.foto



    


    


    

# para prueba
if __name__ == "__main__":

    prueba = producto()
    #prueba.urls('https://www.amazon.es/Moulinex-Multimoulinette-Compact-DJ300110-capacidad/dp/B00I96MAXC/ref=sr_1_50?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=moulinex&qid=1610394421&refinements=p_89%3AMoulinex&rnid=1692911031&s=kitchen&sr=1-50&th=1')

    prueba.urls = 'https://www.amazon.es/Moulinex-Multimoulinette-Compact-DJ300110-capacidad/dp/B00I96MAXC/ref=sr_1_50?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=moulinex&qid=1610394421&refinements=p_89%3AMoulinex&rnid=1692911031&s=kitchen&sr=1-50&th=1'
    
    prueba.datos()
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
    

 
