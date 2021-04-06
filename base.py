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
    info = ( obj.nombre_pro, obj.url_producto, obj.nombre, obj.foto, obj.deseado, obj.pre_min, obj.pre_max, str(obj.precios))

    c, conn = ini()
    c.execute("INSERT INTO producto (nombre_p, url, nombre, foto, deseado, pre_min, pre_max, precios) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info)
    fin(conn)

def editar(obj):
    pos = obj.id_p
    des = obj.deseado
    print(des , "  ", type(des), "<---------------------------------------")
    info = (obj.nombre , des, pos)
    
    c, conn = ini()
    c.execute("UPDATE producto SET nombre = ?, deseado = ? WHERE rowid = ?", [info[0], info[1], int(info[2])])
    fin(conn)

def eliminar(obj):
    c, conn = ini()
    c.execute("DELETE FROM producto  WHERE rowid = ?", [obj.id_p])
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

