from flask import Blueprint
from controllers.venta_controller import cntListado

ventas_bp = Blueprint ('ventas', __name__)


@ventas_bp.route('/')
def listado():
    return cntListado()