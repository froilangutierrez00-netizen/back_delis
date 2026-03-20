from flask import jsonify , request
from  services.cliente_services import listado_cliente


def cntListado():
    datos = listado_cliente()
    print(datos)
