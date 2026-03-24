from flask import jsonify , request
from  services.ventas_services import listado_ventas



def cntListado():
    try:
        datos = listado_ventas()
        return jsonify(datos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500