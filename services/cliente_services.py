from flask import current_app
from models.cliente_model import cliente


def listado_cliente():
    c = current_app.mysql.connection.cursor()
    sql = "select * from cliente"
    c.execute(sql)
    datos = c.fetchall()
    print(datos)
    x=[]
    for p in datos:
        diccionario = cliente(id=p[0],
				 nombre=p[1],celular=p[3],correo=p[4], apellido=p[2]).toDic()
        x.append(diccionario)
    
    return x

    