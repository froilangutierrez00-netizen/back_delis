from flask import blueprint
from controllers.cliente_controler import cntListado

cliente_bp = blueprint ('cliente', __name__)


@cliente_bp.route('/')
def listado():
    return cntListado()