# __init__.py
from .clientes import cliente_bp
# from .roles import roles_bp

def cargarRuta(app):
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    # app.register_blueprint(roles_bp, url_prefix='/roles')



    # http://10.0.0.5:5000/productos
    # http://10.0.0.5:5000/roles