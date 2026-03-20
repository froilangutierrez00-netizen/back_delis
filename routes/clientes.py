from flask import Blueprint
from controllers.cliente_controler import cntListado

cliente_bp = Blueprint ('cliente', __name__)


@cliente_bp.route('/')
def listado():
    return cntListado()