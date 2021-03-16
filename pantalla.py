import tkinter 


def base():
    root = tkinter.Tk()
    root.title("PRECIOS")
    root.config(bg = "grey")

    return root

def grafica(base):
    fondo = tkinter.Frame(base, padx = 5, pady = 5, bg = "black", width = 400, height = 300 )
    fondo.grid(row = 0, column = 0, sticky = "NSEW")
    base.rowconfigure( 0, weight = 1)
    base.columnconfigure(0, weight = 2)

#datos productos
def obj_info(base, produc):
    objs = tkinter.Frame(base, padx = 5, pady = 5)
    objs.config( bg = "blue")
    objs.grid(row = 0, column = 1, rowspan = 2, sticky = "NSEW")
    base.columnconfigure( 1, weight = 1)
    fot(objs, produc)
    nombre_pro(objs, produc)
    precios_pro(objs, produc)
    botones(objs, produc)

#componentes de datos productos
def fot(base, produc):
    holder = tkinter.Frame( base, bg = "white")
    holder.grid(row = 0, column = 0, columnspan = 2, sticky = "NSEW")
    base.rowconfigure(0, weight = 1, minsize = 100)
    base.columnconfigure(0, weight = 1 )
    base.columnconfigure(1, weight = 1)

    base.update_idletasks()
    wdx = holder.winfo_width()
    print(wdx)

    spc = tkinter.Label(base, bg = "black")
    spc.grid(row = 1)

def nombre_pro(base, produc):
    nom = tkinter.Label(base, text = "PRODUCTO")
    nom.grid( row = 2, column = 0, columnspan = 2, sticky = "w")

    variable = tkinter.StringVar(base)
    variable.set(producto[0])
    lista = tkinter.OptionMenu(base, variable, *produc)
    lista.grid( row = 3, column = 0, columnspan = 2, sticky = "ew")

def precios_pro(base, produc):
    precio_ac = tkinter.Label(base, text = "PRECIO")
    precio_ac.grid(row = 4, column = 0, columnspan = 2, sticky = "w")

    pre_act = tkinter.StringVar(base)#cambiar produc precio
    pre_act.set(produc[0])
    prel = tkinter.Label(base, textvariable = pre_act)
    prel.grid(row = 5, column = 0, columnspan = 2, sticky ="w")

    deseo = tkinter.Label(base, text = "PRECIO DESEADO")
    deseo.grid(row = 6, column = 0, columnspan = 2, sticky = "w")

    des = tkinter.StringVar(base)
    des.set(produc[1])#cambiar llamada al producto
    desl = tkinter.Label(base, textvariable = des)
    desl.grid(row = 7, column = 0, columnspan= 2, sticky = "w")

def precios(base):
    pass

def botones(base, produc):
    bt1 = tkinter.Button(base, text="-act-")
    bt2 = tkinter.Button(base, text="editar")
    bt1.grid(row = 8, column = 0, sticky = "S")
    bt2.grid(row = 8, column = 1, sticky = "S")

#cudros datos 
def historico(base, valores):
    cuadro = tkinter.LabelFrame(base, padx = 5, pady = 5, bg = "green")
    cuadro.grid( row = 1, column = 0, sticky = "NSEW")

    lmx = tkinter.Label(cuadro, text = "MAXIMO: ")
    mx = tkinter.Label(cuadro, text = valores[0])
    lmx.grid(row = 0, column = 0, sticky = "w")
    mx.grid( row = 0, column = 1)

    lpm = tkinter.Label(cuadro, text = "PROMEDIO: ")
    pm = tkinter.Label(cuadro, text = valores[1])
    lpm.grid(row = 1, column = 0, sticky = "W")
    pm.grid( row = 1, column = 1)

    lmn = tkinter.Label(cuadro, text = "MINIMO: ")
    mn = tkinter.Label(cuadro, text = valores[2])
    lmn.grid(row = 2, column = 0, sticky = "W")
    mn.grid( row = 2, column = 1)




if __name__ == "__main__":

    valores = ["-----,--  --/--/--", "-----,--  --/--/--", "-----,--  --/--/--"]
    producto = ["1", "2"]
    
    raiz = base()
    raiz.update_idletasks()
    grafica(raiz)
    obj_info(raiz, producto )
    historico(raiz, valores)

    raiz.mainloop()
