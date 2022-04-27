from gestion.zona import Zona
class Zoologico:
    def __init__ (self,nombre=None,ubicacion=None):

        
        self._nombre=nombre
        self._ubicacion= ubicacion
        self._zonas=None

    def agregarZonas(self,zonas):
        self._zona=[]
        self._zona.append(zonas)



    def cantidadTotalAnimales(self):
        self._zona=[]
        Nzonas=0
        for i in self._zonas:
            Nzonas+=i.cantidadAnimales()
        return Nzonas
      
    
    def getNombre(self):

        return self._nombre

    def setNombre(self,nombre):

        self._nombre=nombre

    def getUbicacion(self):
         return self._ubicacion
    
    def getZona(self):
        return self._zonas
        