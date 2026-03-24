# __init__.py
from .ventas import ventas_bp
# from .roles import roles_bp

def cargarRuta(app):
    app.register_blueprint(ventas_bp, url_prefix='/ventas')
    # app.register_blueprint(roles_bp, url_prefix='/roles')



    # http://10.0.0.5:5000/productos
    # http://10.0.0.5:5000/roles