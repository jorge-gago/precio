import productos as pro
import base 

obj = pro.producto()
lista_p = ""

def nuevo():
    base.crear(obj)
    llamar()

def llamar():
    global lista_p
    lista_p = base.lista()

def llamar_producto( id):
    pass

def edit_bas():
    base.editar(obj)
    llamar()
    
def eliminar(id):
    obj.id_p = id
    base.eliminar(obj)
    llamar()


# inicio de loop
if __name__ == "__main__":
    base.primera_llamada()
    llamar()
    #nuevo()

    for i in lista_p:
        print(i)
    print("")
    print(obj.al())
    new = lista_p[2]
    print(new)
    obj.change(new)
    #print(obj.al())
    

