import urls

data = ""

def buscar( nombre, inicio = 0):
    obj = data[inicio:].find(nombre)
    return obj

def precio( ref):
    lugar = buscar(ref)
    final = lugar + (buscar("&", lugar))
    precio_final = data[lugar: final] 
    print (lugar, " ", final)
    return precio_final



if __name__ == "__main__":

    url_test1 = "https://www.amazon.es/Moulinex-Multimoulinette-Compact-DJ300110-capacidad/dp/B00I96MAXC/ref=sr_1_50?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=moulinex&qid=1610394421&refinements=p_89%3AMoulinex&rnid=1692911031&s=kitchen&sr=1-50"

    precio_descuento ='id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">24,99&nbsp;€</span>'
   
    data =str( urls.llamadas_url( url_test1))
    print (data)
    #print(precio (precio_descuento))
    #print("fin")