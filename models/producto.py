class producto:
    def _init_(self,ID,NOMBRE,PRECIO,UNIDAD):
        self.ID_PRODUCTO        = ID
        self.PRO_NOMBRE         = NOMBRE
        self.PRECIO_VENTA       = PRECIO
        self.PRO_UNIDAD_MEDIDA  = UNIDAD

    def toDic(self):
        return{
            "ID_PRODUCTO":self.ID_PRODUCTO,
            "PRO_NOMBRE":self.PRO_NOMBRE,
            "PRECIO_VENTA": self.PRECIO_VENTA,
            "PRO_UNIDAD_MEDIA": self.PRO_UNIDAD_MEDIDA,
            }
        