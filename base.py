import sqlite3

def ini():
    conn = sqlite3.connect('productos.db')
    c = conn.cursor()
    return c, conn

def primera_llamada():
    c, conn = ini()
    c.execute("""CREATE TABLE IF NOT EXISTS producto(
        nombre_p TEXT,
        url TEXT,
        nombre TEXT,
        foto BLOB,
        deseado REAL,
        pre_min REAL,
        pre_max REAL,
        precios BLOB)
        """)
    fin(conn)

def crear(obj):

    print(obj.nombre)
    print(obj.nombre_pro)
    print("------------------------")

    c, conn = ini()
    c.execute("INSERT INTO producto VALUES ( obj.nombre_pro, obj.url_producto, obj.nombre, obj.foto, obj.deseado, obj.pre_min, obj.pre_max, obj.precios)".format (( obj.nombre_pro, obj.url_producto, obj.nombre, obj.foto, obj.deseado, obj.pre_min, obj.pre_max, obj.precios)))
    fin(conn)

def editar(obj):
    c, conn = ini()
    c.execute("UPDATE producto SET nombre = obj.nombre , deseado = obj.deseado   WHERE rowid = obj.id_p")
    fin(conn)

def eliminar(obj):
    c, conn = ini()
    c.execute("DELETE FROM producto  WHERE rowid = obj.id_p")
    fin(conn)

def lista(): #devuelve todos los productos en la db
    c, conn = ini()
    c.execute("SELECT rowid, * FROM producto")
    items = c.fetchall()
    fin(conn)

    return items

def fin(conn):
    conn.commit()
    conn.close()

