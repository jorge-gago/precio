"""with open("D:\escritorio\precios.txt", errors = "ignore") as f:
    datos = f.read()
    print("base")

    if "35." in datos : 
        print("si")
        pos = datos.find("35.")
        print(pos)
        print(datos[pos-100:pos+200])

#print(datos)
print("base")
"""

test1 = '<span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">35,17&nbsp;€</span>'
t1 = test1[:-19]


test2 = '<span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">69,95&nbsp;€</span>'
t2 = test2[:95] #95 largo etiqueta
print(t1)
print(len(test1))
print(t2)

if t1 == t2 : print("true")